#!/usr/bin/env python3
'''
Simple MIDI bridge for NSX-1(eVY1 board, NSX-39)
'''
from argparse import ArgumentParser
import mido
import sys

class Nsx1():
    def __init__(self, debug):
        self.index = 0
        self.solfa_mode = True
        self.lyrics = ''
        self.solfa = 'd o,d o,4 e,4 e,m i,p a,p a,s o,s o,4 a,4 a,s i'
        self.debug = debug
        if self.debug:
            print(mido.backend)
        self.input_names = mido.get_input_names()
        self.output_names = mido.get_output_names()
        self.input_port = None
        self.output_ports = []

    def _pa2list(self, pastr):
        pas = pastr.split(',')
        palst = []
        for pa in pas:
            lst = []
            for c in pa:
                lst.append(ord(c))
            palst.append(lst)
        return palst

    def _print_ports(self, name, ports):
        print(name)
        for i in range(len(ports)):
            print(' {}: {}'.format(i, ports[i]))

    def show_ports(self):
        self._print_ports('Input', self.input_names)
        self._print_ports('Output', self.output_names)

    def input_callback(self, message):
        if message.type == 'note_on':
            if self.solfa_mode:
                data = [0x43, 0x79, 0x09, 0x00, 0x50, 0x10] + self._pa2list(self.solfa)[message.note % 12] + [0x00]
            else:
                lyrics = self._pa2list(self.lyrics)
                data = [0x43, 0x79, 0x09, 0x00, 0x50, 0x10] + lyrics[self.index % len(lyrics)] + [0x00]
                self.index = self.index + 1
            sysex = mido.Message('sysex', data=data)

            if self.debug:
                print(sysex)
            for port in self.output_ports:
                port.send(sysex)

        if self.debug:
            print(message)
        for port in self.output_ports:
            port.send(message)

    def set_route(self, route):
        inp, outp = route.split(':')
        outps = outp.split(',')

        self.input_port = mido.open_input(self.input_names[int(inp)], callback=self.input_callback)
        for op in outps:
            output_port = mido.open_output(self.output_names[int(op)])
            # GM ON
            msg = mido.Message('sysex', data=[0x7e, 0x7f, 0x09, 0x01])
            output_port.send(msg)
            # XG ON
            msg = mido.Message('sysex', data=[0x43, 0x10, 0x4c, 0x00, 0x00, 0x7e, 0x00])
            output_port.send(msg)
            self.output_ports.append(output_port)

    def set_lyrics(self, lyrics):
        self.solfa_mode = False
        self.lyrics = lyrics
        self.index = 0

    def set_solfa(self):
        self.solfa_mode = True

def getArgs():
    usage = 'python3 midi-bridge.py -route 1:0 [-lyrics "a a,k e,m a,s i,t e,o o,m e,d e,t o,M M"]'
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('-route', nargs='?', type=str, dest='route', help='midi msg route: 1:2[,3...]')
    argparser.add_argument('-lyrics', nargs='?', type=str, dest='lyrics', help='lyrics (optional)')
    argparser.add_argument('-debug', action='store_true', dest='debug', help='debug flag')
    return argparser.parse_args()

def main():
    args = getArgs()
    nsx = Nsx1(args.debug)
    if args.route == None:
        nsx.show_ports()
        input_port = input('select input port: ')
        output_port = input('select output port: ')
        nsx.set_route('{}:{}'.format(input_port, output_port))
    else:
        nsx.set_route(args.route)

    if args.lyrics:
        nsx.set_lyrics(args.lyrics)

    while True:
        lyrics = input('new lyrics: ')
        if lyrics == 'quit' or lyrics == 'exit':
            sys.exit()
        elif lyrics == 'solfa':
            print('solfa mode')
            nsx.set_solfa()
        else:
            nsx.set_lyrics(lyrics)

if __name__ == '__main__':
    main()

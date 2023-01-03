# midi-bridge-for-nsx1
Simple MIDI bridge for NSX-1 (eVY1 board, NSX-39(Vol+,Vol-,U))

## Setup
    $ pip3 install -r requirements.txt
    Note: python-rtmidi requires build tools.

## Usage
Select keyboard as input and NSX-1 as output, then play it.

    $ python3 ./midi-bridge.py
    Input
     0: microKEY-25 0
     1: eVY1 MIDI 1
    Output
     0: Microsoft GS Wavetable Synth 0
     1: microKEY-25 1
     2: eVY1 MIDI 2
    select input port: 0
    select output port: 2
    lyrics:

## Lyrics
The default is solfa mode. If you specify lyrics in the form of phonetic alphabet, the lyrics are sung at each keyboard press.

    lyrics: h a,ts M,n e,m i,k M

## Phonetic Alphabet
Below is a partial table of eVocaloid<sup>TM</sup> Phonetic Alphabet(PA) from NSX-1 Specification

    Kana PA    Kana PA    Kana PA    Kana PA    Kana PA
    a    a     i    i     u    M     e    e     o    o
    ka   k a   ki   k' i  ku   k M   ke   k e   ko   k o
    sa   s a   si   S i   su   s M   se   s e   so   s o
    ta   t a   ti   tS i  tu   ts M  te   t e   to   t o
    na   n a   ni   J i   nu   n M   ne   n e   no   n o
    ha   h a   hi   C i   fu   p\ M  he   h e   ho   h o
    ma   m a   mi   m' i  mu   m M   me   m e   mo   m o
    ra   4 a   ri   4' i  ru   4 M   re   4 e   ro   4 o
    ga   g a   gi   g' i  gu   g M   ge   g e   go   g o
    za   dz a  zi   dZ i  zu   dz M  ze   dz e  zo   dz o
    da   d a   di   dZ i  du   dz M  de   d e   do   d o
    ba   b a   bi   b' i  bu   b M   be   b e   bo   b o
    pa   p a   pi   p' i  pu   p M   pe   p e   po   p o
    ya   j a              yu   j M              yo   j o
    wa   w a   wi   w i              we   w e   wo   o

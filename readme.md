# Tindchecker
Brukes for å finne en tekst/id i tind sine systemer.

Kjøres slik:
`python tindcheck.py inputfil outputfil`

## Inputfil
Input er en liste med tekst/id som f.eks:
```
79b007561
79b007604
79b007609
79b007610
Sang for Harmonien i Anledning
Om Baldandse i Almindelighed og
KlŸwer-Familiens Historie af Lorentz Diderich
```

## Outputfil
```
79b007604;246762;Beskrivelse over Nummedahl og Sandswerd;Flor, Hans Zacharias
80b012892;246779;Antiqvariske Iagttagelser paa en Reise gjennem Deele af  det Norden og Søndenfjeldske Norge i Aaret 1823. Norske  Mindesmærker samlede 1823;Klüwer, Lorentz Diderich
84b009549;156354;Olav Trygvessøn-monumentet og dets oprindelse :  dokumenter m.v. samlet i forbindelse med monumentets  tilblivelse;None
84b013175;149688;Dend M**** Orden med alle sine Hemmeligheder, som bruges i  en ret M**** Loge, oversat af det Franske i det Tydske og  deraf igen i det Danske Sprog;None
88b005843;246731;[Tale om Oprindelsen til det Onde i Verden];Gunnerus, Johan Ernst
94b011312;246745;Kurze Betrachtung über die Etiquette;Hennings, Justus Christian
94b032488;107967;Ode de la paix;Ronsard, Pierre de;140365;Les quatre premiers livres des Odes de Pierre de Ronsard,  Vandomois, ensemble son Bocage ...;Ronsard, Pierre de
```
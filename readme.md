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
fant treff;79b007561;257885;Beskrivelse over Hitterens Præstegield i Stor-Fosens  Provstie, under Trondhjems Stift i Norge af Peder Schwane  Bang;None;Bang, Peder Schwane
fant treff;79b007604;246762;Beskrivelse over Nummedahl og Sandswerd / forfattet af  Hans Zacharias Flor og Christian Sthyr;None;Flor, Hans Zacharias and Styr, Christen
fant treff;79b007609;257979;Beskrivelse over Brønøy Præstegield paa Helleland i  Nordlandene. Kort Beskrivelse over Brønøe Præstegield  udi Nordlandene;None;None
fant treff;79b007610;257980;Een kort Efterretning af Numedahls Fogderies oeconomiske  Tilstand i Tronhejms Amt i Henseende til Agerdyrkningen,  Fiskeriene og Handelen / J. M. Lund;None;Lund, Johan Michael
fant treff;Sang for Harmonien i Anledning;258328;Sang for Harmonien i Anledning af Hans Majestæt Kong  Christian Frederiks Tronbestigelse;None;None
fant treff;Om Baldandse i Almindelighed og;258329;Om Baldandse i Almindelighed og franske quadriller i  særdeleshed af E. Hall;None;Hald, A.
ikke funnet;KlÅ¸wer-Familiens Historie af Lorentz Diderich
```
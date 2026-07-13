# Password Strength Checker

Prvý miniprojekt na mojej ceste k Python/AI engineeringu.
Nástroj, ktorý vyhodnotí silu zadaného hesla na základe 6 pravidiel.

## Čo program robí
Skontroluje heslo a pridelí skóre 0–6 podľa splnených kritérií:
- Dĺžka aspoň 8 znakov
- Obsahuje veľké písmeno
- Obsahuje malé písmeno
- Obsahuje číslicu
- Obsahuje špeciálny znak
- Nie je medzi častými (ľahko uhádnuteľnými) heslami

Program beží v slučke, kým používateľ nezadá dostatočne silné heslo.

## Ako spustiť
```bash
python password_checker.py
```

> Pozn.: Heslo sa zadáva skryto cez knižnicu `getpass`
> (pri písaní nie je viditeľné). Spúšťaj cez terminál.

## Použité koncepty
- Funkcie a return hodnoty
- Cykly (for, while) a early return pattern
- Podmienky (if/elif/else)
- String metódy (isupper, islower, isdigit)
- Zoznamy a `in` operátor
- Import knižnice (getpass)

## Čo som sa naučil
- Rozdelenie logiky do samostatných funkcií
- Práca so string metódami na analýzu znakov
- Prvý import knižnice a použitie getpass
- Formátovanie kódu pomocou black
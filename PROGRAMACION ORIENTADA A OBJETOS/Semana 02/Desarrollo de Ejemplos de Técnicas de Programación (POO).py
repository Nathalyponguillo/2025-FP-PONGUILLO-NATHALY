# python
from rich.console import Console
from rich.table import Table
import time
import sys

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        if not self.esta_vivo():
            print(self.nombre, "no puede actuar: está fuera de combate")
            return
        daño = self.daño(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        try:
            opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        except ValueError:
            print("Entrada no válida")
            return
        if opcion == 1:
            self.espada = 8
            print(self.nombre, "ha equipado Acero Valyrio (8)")
        elif opcion == 2:
            self.espada = 10
            print(self.nombre, "ha equipado Matadragones (10)")
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return max(0, self.inteligencia * self.libro - enemigo.defensa)

class GameCLI:
    """
    Interfaz CLI visual con rich.
    - Muestra una tabla con estado de los personajes.
    - Permite elegir acción (atacar, cambiar arma si aplica, ver atributos, salir).
    """
    def __init__(self, jugador_1, jugador_2):
        self.console = Console()
        self.j1 = jugador_1
        self.j2 = jugador_2
        self.turno = 1

    def _tabla_estado(self):
        t = Table(title="Estado de Personajes")
        t.add_column("Nombre", justify="left")
        t.add_column("Vida", justify="right")
        t.add_column("Fuerza", justify="right")
        t.add_column("Inteligencia", justify="right")
        t.add_column("Defensa", justify="right")
        t.add_column("Extra", justify="left")
        for p in (self.j1, self.j2):
            extra = ""
            if hasattr(p, "espada"):
                extra = f"Espada={p.espada}"
            if hasattr(p, "libro"):
                extra = f"Libro={p.libro}"
            t.add_row(p.nombre, str(p.vida), str(p.fuerza), str(p.inteligencia), str(p.defensa), extra)
        return t

    def _elegir_accion(self, actor):
        opciones = ["1) Atacar", "2) Ver atributos"]
        if isinstance(actor, Guerrero):
            opciones.insert(1, "3) Cambiar arma")
        opciones.append("0) Salir")
        self.console.print("Acciones: " + " | ".join(opciones))
        elección = self.console.input("Elige acción: ").strip()
        return elección

    def _procesar(self, actor, rival, elección):
        if elección == "0":
            self.console.print("Saliendo...")
            sys.exit(0)
        if elección == "1":
            actor.atacar(rival)
        elif elección == "2":
            actor.atributos()
        elif elección == "3" and isinstance(actor, Guerrero):
            actor.cambiar_arma()
        else:
            self.console.print("[red]Opción inválida[/red]")

    def run(self):
        while self.j1.esta_vivo() and self.j2.esta_vivo():
            self.console.clear()
            self.console.print(self._tabla_estado())
            actor = self.j1 if self.turno % 2 == 1 else self.j2
            rival = self.j2 if actor is self.j1 else self.j1
            self.console.print(f"\n--- Turno {self.turno} : {actor.nombre} ---")
            if not actor.esta_vivo():
                self.console.print(f"{actor.nombre} está fuera de combate y pierde el turno")
            else:
                elección = self._elegir_accion(actor)
                self._procesar(actor, rival, elección)
            time.sleep(0.6)
            if not rival.esta_vivo():
                break
            self.turno += 1

        self.console.print("\n=========================== Fin ===========================")
        if self.j1.esta_vivo() and not self.j2.esta_vivo():
            self.console.print(f"[green]Ha ganado {self.j1.nombre}[/green]")
        elif self.j2.esta_vivo() and not self.j1.esta_vivo():
            self.console.print(f"[green]Ha ganado {self.j2.nombre}[/green]")
        else:
            self.console.print("[yellow]Empate[/yellow]")

if __name__ == "__main__":
    personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
    personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)
    cli = GameCLI(personaje_1, personaje_2)
    cli.run()
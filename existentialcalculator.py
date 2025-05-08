import random
from collections import Counter

class ExistentialCalculator:
    def __init__(self):
        self.aspects = {
            "significado": ["encontrar propósito", "conectar con otros", "crear algo valioso", "experimentar la vida", "no hay significado inherente"],
            "propósito": ["contribuir al bien común", "evolucionar personalmente", "disfrutar el presente", "dejar un legado", "no hay propósito predefinido"],
            "felicidad": ["bienestar emocional", "satisfacción con la vida", "momentos de alegría", "aceptación", "una búsqueda constante"],
            "conexión": ["familia", "amigos", "comunidad", "la naturaleza", "uno mismo"],
            "legado": ["hijos", "obra creativa", "impacto social", "memorias", "nada perdura"],
        }
        self.weights = {aspect: [0.2, 0.2, 0.2, 0.2, 0.2] for aspect in self.aspects} # Distribución uniforme inicial

    def set_user_weights(self, user_priorities):
        """Permite al usuario influir en las probabilidades de cada aspecto."""
        for aspect, priority in user_priorities.items():
            if aspect in self.aspects and isinstance(priority, (list, tuple)) and len(priority) == len(self.aspects[aspect]):
                # Normalizar las prioridades del usuario para que sumen 1 (aproximadamente)
                total_priority = sum(priority)
                if total_priority > 0:
                    self.weights[aspect] = [p / total_priority for p in priority]
                else:
                    self.weights[aspect] = [1.0 / len(self.aspects[aspect])] * len(self.aspects[aspect])
            else:
                print(f"Advertencia: Prioridades inválidas para '{aspect}'. Usando distribución predeterminada.")

    def calculate_existential_tendencies(self, num_samples=1000):
        """Simula la 'tendencia' existencial basada en las probabilidades."""
        results = {aspect: [] for aspect in self.aspects}
        for _ in range(num_samples):
            for aspect, options in self.aspects.items():
                chosen_option = random.choices(options, weights=self.weights[aspect], k=1)[0]
                results[aspect].append(chosen_option)
        return {aspect: Counter(options).most_common(3) for aspect, options in results.items()}

    def provide_existential_insights(self, tendencies):
        """Ofrece interpretaciones basadas en las tendencias calculadas."""
        print("\n--- Perspectivas Existenciales ---")
        for aspect, top_tendencies in tendencies.items():
            print(f"\nSegún tus ponderaciones, tu tendencia hacia el '{aspect}' parece inclinarse hacia:")
            for option, probability in top_tendencies:
                print(f"- '{option}' (con una frecuencia relativa)") # No es una probabilidad real aquí
            if aspect == "significado" and any("no hay significado inherente" in item for item, _ in top_tendencies):
                print("  Es importante recordar que la ausencia de un significado inherente no implica la ausencia de un significado creado o encontrado.")
            elif aspect == "propósito" and any("no hay propósito predefinido" in item for item, _ in top_tendencies):
                print("  La falta de un propósito predefinido te otorga la libertad de definir el tuyo propio.")
            elif aspect == "felicidad" and any("una búsqueda constante" in item for item, _ in top_tendencies):
                print("  La felicidad a menudo se experimenta en el viaje, no solo en el destino.")

    def run(self):
        print("--- Calculadora Existencial ---")
        print("Por favor, indica tu nivel de importancia (de 0 a 10) para las siguientes perspectivas:")
        user_priorities = {}
        for aspect, options in self.aspects.items():
            print(f"\nAspecto: {aspect.capitalize()}")
            priorities = []
            for i, option in enumerate(options):
                while True:
                    try:
                        importance = int(input(f"  Importancia de '{option}': "))
                        if 0 <= importance <= 10:
                            priorities.append(importance / 10.0) # Convertir a una escala de probabilidad relativa
                            break
                        else:
                            print("Por favor, ingresa un valor entre 0 y 10.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingresa un número entero.")
            user_priorities[aspect] = priorities

        self.set_user_weights(user_priorities)
        tendencies = self.calculate_existential_tendencies()
        self.provide_existential_insights(tendencies)

if __name__ == "__main__":
    calculator = ExistentialCalculator()
    calculator.run()
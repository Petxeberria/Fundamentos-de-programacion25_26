#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * Función que simula el lanzamiento de un dado tradicional de 6 caras.
 * @return Un número entero aleatorio entre 1 y 6.
 */
int tirar_dado() {
    return rand() % 6 + 1;
}

/**
 * Función que simula el lanzamiento de una moneda con valores 2 o 3.
 * @return Un número entero aleatorio: 2 o 3.
 */
int tirar_moneda() {
    return rand() % 2 + 2;
}

/**
 * Función que determina si la acción del número 6 será multiplicar o dividir.
 * @return 1 para multiplicar, 0 para dividir.
 */
int tipo_operacion() {
    return rand() % 2;
}

/**
 * Función que maneja el turno del jugador humano.
 * Acumula puntos mediante tiradas de dados y decide cuándo plantarse.
 * @param puntos_oponente Puntero a los puntos de la máquina para restarle el daño acumulado al final.
 */
void turno_jugador(int *puntos_oponente) {
    int acumulado = 0;
    char eleccion;

    printf("\n--- TU TURNO ---\n");
    while (1) {
        int tirada = tirar_dado();
        printf("Has sacado un: %d\n", tirada);

        if (tirada == 1) {
            printf("¡Vaya! Has sacado un 1. Pierdes el turno y los puntos acumulados.\n");
            acumulado = 0;
            break; // Se pierde el turno inmediatamente
        } else if (tirada >= 2 && tirada <= 5) {
            acumulado += tirada;
            printf("Sumas %d puntos. Acumulado parcial: %d\n", tirada, acumulado);
        } else if (tirada == 6) {
            int op = tipo_operacion();
            int valor = tirar_moneda();
            if (op == 1) {
                acumulado *= valor;
                printf("¡Sacaste un 6! Multiplicador x%d. Nuevo acumulado: %d\n", valor, acumulado);
            } else {
                acumulado /= valor; // La división entre enteros en C redondea hacia abajo automáticamente
                printf("¡Sacaste un 6! Divisor /%d. Nuevo acumulado: %d\n", valor, acumulado);
            }
        }

        // Interfaz de preguntas requerida por las reglas
        printf("¿Quieres seguir tirando? (s/n): ");
        scanf(" %c", &eleccion);
        if (eleccion == 'n' || eleccion == 'N') {
            break; // El jugador decide parar
        }
    }

    // Se le restan los puntos finales al oponente
    *puntos_oponente -= acumulado;
    printf("Termina tu turno. Le quitas %d puntos a la maquina.\n", acumulado);
}

/**
 * Función que maneja el turno de la máquina oponente (Inteligencia Artificial básica).
 * Estrategia: Tira dados sin parar hasta acumular 7 o más puntos, o hasta sacar un 1.
 * @param puntos_oponente Puntero a los puntos del jugador para restarle el daño acumulado.
 */
void turno_maquina(int *puntos_oponente) {
    int acumulado = 0;
    printf("\n--- TURNO DE LA MAQUINA ---\n");

    // La máquina se arriesga hasta tener al menos 7 puntos
    while (acumulado < 7) {
        int tirada = tirar_dado();
        printf("La maquina saca un: %d\n", tirada);

        if (tirada == 1) {
            printf("La maquina saco un 1 y pierde sus puntos acumulados.\n");
            acumulado = 0;
            break; // Termina el turno de la máquina
        } else if (tirada >= 2 && tirada <= 5) {
            acumulado += tirada;
            printf("La maquina suma %d (Acumulado: %d).\n", tirada, acumulado);
        } else if (tirada == 6) {
            int op = tipo_operacion();
            int valor = tirar_moneda();
            if (op == 1) {
                acumulado *= valor;
                printf("La maquina saco un 6. Multiplicador x%d (Acumulado: %d).\n", valor, acumulado);
            } else {
                acumulado /= valor;
                printf("La maquina saco un 6. Divisor /%d (Acumulado: %d).\n", valor, acumulado);
            }
        }
    }

    // Se le restan los puntos finales al jugador
    *puntos_oponente -= acumulado;
    printf("Termina el turno de la maquina. Te quita %d puntos.\n", acumulado);
}

int main() {
    // Inicializar la semilla para la generación de números aleatorios
    srand(time(NULL));

    // Condiciones iniciales de la partida
    int puntos_jugador = 100;
    int puntos_maquina = 100;

    printf("=== BIENVENIDO AL JUEGO DE DADOS ===\n");
    printf("Ambos jugadores comienzan con 100 puntos. ¡El primero en llegar a 0 o menos pierde!\n");

    // Bucle principal del juego de turnos
    while (puntos_jugador > 0 && puntos_maquina > 0) {
        printf("\n========================================\n");
        printf("MARCADOR ACTUAL -> Jugador: %d | Maquina: %d\n", puntos_jugador, puntos_maquina);
        printf("========================================\n");

        // Turno del Jugador
        turno_jugador(&puntos_maquina);

        // Si el jugador hace que la máquina llegue a 0, se rompe el ciclo para no jugar el turno de la máquina
        if (puntos_maquina <= 0) {
            break; 
        }

        // Turno de la Máquina
        turno_maquina(&puntos_jugador);
    }

    // Declaración del ganador de acuerdo a las reglas
    printf("\n========================================\n");
    printf("MARCADOR FINAL -> Jugador: %d | Maquina: %d\n", puntos_jugador, puntos_maquina);
    printf("========================================\n");
    
    if (puntos_jugador <= 0) {
        printf("¡LA MAQUINA GANA! Te has quedado sin puntos.\n");
    } else {
        printf("¡FELICIDADES! ¡HAS GANADO LA PARTIDA!\n");
    }

    return 0;
}
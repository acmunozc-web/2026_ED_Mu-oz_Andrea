import java.util.ArrayList;
import java.util.Scanner;


// Clase Contacto: representa un registro con atributos heterogéneos
class Contacto {
    String nombre;
    String telefono;
    String correo;

    Contacto(String nombre, String telefono, String correo) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.correo = correo;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Teléfono: " + telefono + ", Correo: " + correo;
    }
}

// Clase Agenda: estructura que gestiona una colección de contactos
class Agenda {
    ArrayList<Contacto> contactos = new ArrayList<>();

    // Método para agregar un contacto
    void agregarContacto(Contacto c) {
        contactos.add(c);
        System.out.println("Contacto agregado correctamente.");
    }

    // Método para buscar por nombre
    Contacto buscarPorNombre(String nombre) {
        for (Contacto c : contactos) {
            if (c.nombre.equalsIgnoreCase(nombre)) {
                return c;
            }
        }
        return null;
    }

    // Método para mostrar todos los contactos
    void mostrarContactos() {
        if (contactos.isEmpty()) {
            System.out.println("La agenda está vacía.");
        } else {
            System.out.println("Lista de contactos:");
            for (Contacto c : contactos) {
                System.out.println(c);
            }
        }
    }

    // Método para eliminar un contacto
    void eliminarContacto(String nombre) {
        Contacto c = buscarPorNombre(nombre);
        if (c != null) {
            contactos.remove(c);
            System.out.println("Contacto eliminado.");
        } else {
            System.out.println("No se encontró el contacto.");
        }
    }
}

// Clase principal
public class AgendaTelefonica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Agenda agenda = new Agenda();
        int opcion;

        do {
            System.out.println("\n--- Agenda Telefónica ---");
            System.out.println("1. Agregar contacto");
            System.out.println("2. Buscar contacto por nombre");
            System.out.println("3. Mostrar todos los contactos");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Ingrese teléfono: ");
                    String telefono = sc.nextLine();
                    System.out.print("Ingrese correo: ");
                    String correo = sc.nextLine();
                    agenda.agregarContacto(new Contacto(nombre, telefono, correo));
                    break;
                case 2:
                    System.out.print("Ingrese nombre a buscar: ");
                    String buscar = sc.nextLine();
                    Contacto encontrado = agenda.buscarPorNombre(buscar);
                    if (encontrado != null) {
                        System.out.println("Contacto encontrado: " + encontrado);
                    } else {
                        System.out.println("No se encontró el contacto.");
                    }
                    break;
                case 3:
                    agenda.mostrarContactos();
                    break;
                case 4:
                    System.out.print("Ingrese nombre del contacto a eliminar: ");
                    String eliminar = sc.nextLine();
                    agenda.eliminarContacto(eliminar);
                    break;
                case 5:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción inválida.");
            }
        } while (opcion != 5);

        sc.close();
    }
}
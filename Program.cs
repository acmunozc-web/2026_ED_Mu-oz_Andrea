using System;
using System.Collections.Generic;

namespace NavegadorWeb
{
    class HistorialNavegador
    {
        private Stack<string> historial;

        public HistorialNavegador()
        {
            historial = new Stack<string>();
        }

        // Método para visitar una nueva página
        public void VisitarPagina(string url)
        {
            historial.Push(url);
            Console.WriteLine($"Visitando: {url}");
        }

        // Método para retroceder a la página anterior
        public void Retroceder()
        {
            if (historial.Count > 1)
            {
                historial.Pop(); // Elimina la página actual
                Console.WriteLine($"Retrocediendo a: {historial.Peek()}");
            }
            else
            {
                Console.WriteLine("No hay más páginas para retroceder.");
            }
        }

        // Mostrar todo el historial
        public void MostrarHistorial()
        {
            Console.WriteLine("\nHistorial de navegación:");
            foreach (var pagina in historial)
            {
                Console.WriteLine(pagina);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            HistorialNavegador navegador = new HistorialNavegador();

            navegador.VisitarPagina("www.google.com");
            navegador.VisitarPagina("www.microsoft.com");
            navegador.VisitarPagina("www.github.com");

            navegador.MostrarHistorial();

            navegador.Retroceder();
            navegador.Retroceder();

            navegador.MostrarHistorial();
        }
    }
}
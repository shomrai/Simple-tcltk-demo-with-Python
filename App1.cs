using System;
using System.IO;

namespace PopupWindow
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get the title from the first argument passed to the program
            string title = args[0];

            // Display a pop-up window with the given title
            Console.WriteLine("Displaying window with title: " + title);

            // Ask the user to select a directory
            Console.WriteLine("Please select a directory:");
            string directoryPath = GetDirectoryPath();

            // Display the selected directory path
            Console.WriteLine("Selected directory: " + directoryPath);

            // Wait for the user to press a key before exiting
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        static string GetDirectoryPath()
        {
            // Create a new instance of the FolderBrowserDialog class
            System.Windows.Forms.FolderBrowserDialog dialog = new System.Windows.Forms.FolderBrowserDialog();

            // Display the dialog and wait for the user to select a directory
            System.Windows.Forms.DialogResult result = dialog.ShowDialog();

            // If the user clicked OK, return the selected directory path
            if (result == System.Windows.Forms.DialogResult.OK)
            {
                return dialog.SelectedPath;
            }
            // Otherwise, return an empty string
            else
            {
                return "";
            }
        }
    }
}

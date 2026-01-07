import java.io.FileWriter;
import java.io.IOException;
import java.util.Locale;

public class Generador {
    public static void main(String [] args){
        try(FileWriter fw = new FileWriter("Muestras/muestra_java_float.txt")){
            for(int i=0; i<1e6; i++) {
                fw.write(String.format(Locale.US, "%.8f%n", Math.random()));
            }
        } catch (IOException e) {
            System.out.println("Error al escribir el archivo");
            e.printStackTrace();
        }
    }
}
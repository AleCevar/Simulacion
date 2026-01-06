import java.io.FileWriter;
import java.io.IOException;

public class Generador {
    public static void main(String [] args){
        try(FileWriter fw = new FileWriter("Muestras/muestra_java_float.txt")){
            for(int i=0; i<1e6; i++) {
                fw.write(String.valueOf(Math.random())+"\n");
            }
        } catch (IOException e) {
            System.out.println("Error al escribir el archivo");
            e.printStackTrace();
        }
    }
}
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
// import org.apache.commons.io.FileUtils;
// import com.google.common.io.Files;

/** * How to write to a file using try-with-resource statement in Java. * * @author java67 */ 
public class prog2 { 
	public static void main(String args[]) throws IOException {

		String source_path,dest_path;
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter source file (optional: with path)");
		source_path = scan.next();
		System.out.println("Enter destination file (optional: with path)");
		dest_path = scan.next();
		fileOps(dest_path);

		File from = new File(source_path);
		File to = new File(dest_path);

		System.out.println("Copying file into another location");
		copy(from, to);
	} 

	/** * Java 7 way to copy a file from one location to another * @param from * @param to * @throws IOException */ 
	public static void copy(File src, File dest) throws IOException { 
		InputStream is = null; 
		OutputStream os = null; 
		try { 
			is = new FileInputStream(src); 
			os = new FileOutputStream(dest); 
			// buffer size 1K 
			byte[] buf = new byte[1024]; 
			int bytesRead; 
			while ((bytesRead = is.read(buf)) > 0) { 
				os.write(buf, 0, bytesRead); 
			} 
		}
		catch (Exception e){
			System.out.println(e);
		} 
		finally { 
			is.close(); 
			os.close(); 
		} 
	}

	public static void fileOps(String s){
		String[] dirs = s.split("/");
		String path = "";

		for (int i = 0; i < (dirs.length-1) ; ++i){
			path = path + dirs[i] + "/";
		}

		File dir = new File(path);
		dir.mkdirs();
	}


}
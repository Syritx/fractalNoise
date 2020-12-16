import java.io.File;
import java.io.IOException;
import java.util.*;

import javax.imageio.ImageIO;
import java.awt.image.*;


import java.awt.color.*;

public class ImageCreator {
    static List<String> lines = new ArrayList<String>();

    public static void main(String[] args) throws IOException {
        readFile();
    }

    static void readFile() throws IOException {
        String path = "noise.txt";
        File file = new File(path);

        if (!file.exists()) return;
        Scanner scanner = new Scanner(file);

        while (scanner.hasNext()) {
            lines.add(scanner.nextLine());
        }

        int width = 0, height = lines.size();
        width = lines.get(0).split(" ").length;

        List<Float> allpoints = new ArrayList<Float>();
        for (String s : lines) {
            String[] nums = s.split(" ");

            for (String n : nums) {
                float num = Float.parseFloat(n);
                allpoints.add(num);
            }
        }

        createImage(allpoints, width, height);
    }

    static void createImage(List<Float> points, int width, int height) throws IOException {

        BufferedImage image = new BufferedImage(width,height,BufferedImage.TYPE_INT_RGB);
        float[][] vPoints = new float[width][height];

        int pointsId = 0;

        // Converting ArrayList to Array of arrays
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                vPoints[x][y] = points.get(pointsId);
                pointsId++;
            }
        }

        for (int w = 0; w < width; w++) {
            for (int h = 0; h < height; h++) {
                image.setRGB(w, h, (int)(vPoints[w][h]*5));
            }
        }

        File file = new File("result.jpg");
        image = desaturateImage(image);

        ImageIO.write(image,"jpg",file);
    }

    static BufferedImage desaturateImage(BufferedImage image) {
        ColorConvertOp convert = new ColorConvertOp(
            ColorSpace.getInstance(ColorSpace.CS_GRAY),null);
        convert.filter(image, image);

        return image;
    }
}
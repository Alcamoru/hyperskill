// do not remove imports
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.function.Function;

class ArrayUtils {
    // define hasNull method here

    public static <T> boolean hasNull(T[] array) {
        List<T> elist = new ArrayList<>(Arrays.asList(array));
        return elist.contains(null);
    }
}
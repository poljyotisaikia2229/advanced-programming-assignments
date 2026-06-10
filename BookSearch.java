import java.util.ArrayList;

public class BookSearch {

    public static void main(String[] args) {

        ArrayList<String> books = new ArrayList<String>();

        books.add("Java Programming");
        books.add("Data Structures");
        books.add("Python Basics");
        books.add("Advanced Java");
        books.add("Web Development");

        String searchWord = "Java";

        System.out.println("Books containing the word \"" + searchWord + "\":\n");

        for (String book : books) {
            if (book.toLowerCase().contains(searchWord.toLowerCase())) {
                System.out.println(book);
            }
        }
    }
}
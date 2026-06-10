import java.util.*;
import java.util.stream.*;

class Student {

    private int id;
    private String name;
    private List<String> courses;
     
    private Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public int getId() { return id; }

    public String getName() { return name; }

    public List<String> getCourses() { return courses; }

    public Map<String, Integer> getScores() { return scores; }

    public double getAverageScore() {
        return scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0.0);
    }
}

class StudentPerformanceAnalyzer {

    public static List<Student> getTopStudents(List<Student> students, int n) {

        return students.stream()
                .sorted((a, b) ->
                        Double.compare(b.getAverageScore(), a.getAverageScore()))
                .limit(n)
                .toList();
    }

    public static Map<String, Double> getCourseAverages(List<Student> students) {

        return students.stream()
                .flatMap(s -> s.getCourses()
                        .stream()
                        .map(c -> Map.entry(c, s.getScores().get(c))))
                .collect(Collectors.groupingBy(
                        Map.Entry::getKey,
                        Collectors.averagingInt(Map.Entry::getValue)
                ));
    }

    public static Set<String> getUniqueCourses(List<Student> students) {

        return students.stream()
                .map(Student::getCourses)
                .flatMap(List::stream)
                .collect(Collectors.toSet());
    }
}

public class Assignment6 {

    public static void main(String[] args) {

        long start = System.nanoTime();

        Random random = new Random();

        List<String> allCourses =
                List.of("Math", "Physics", "Chemistry", "Biology", "CS");

        List<Student> students = IntStream.rangeClosed(1, 50)
                .mapToObj(i -> {

                    List<String> shuffled = new ArrayList<>(allCourses);
                    Collections.shuffle(shuffled);

                    List<String> selected = shuffled.subList(0, 3);

                    Map<String, Integer> scores =
                            selected.stream()
                                    .collect(Collectors.toMap(
                                            c -> c,
                                            c -> random.nextInt(41) + 60
                                    ));

                    return new Student(
                            i,
                            "Student " + i,
                            selected,
                            scores
                    );
                })
                .toList();

        List<Student> top =
                StudentPerformanceAnalyzer.getTopStudents(students, 5);

        System.out.println("Top Students:");
        top.forEach(s ->
                System.out.println(s.getName() + " Avg: " + s.getAverageScore()));

        System.out.println("\nCourse Averages:");
        StudentPerformanceAnalyzer.getCourseAverages(students)
                .forEach((c, a) -> System.out.println(c + " -> " + a));

        System.out.println("\nUnique Courses:");
        StudentPerformanceAnalyzer.getUniqueCourses(students)
                .forEach(System.out::println);

        long end = System.nanoTime();

        System.out.println("\nExecution Time: " + (end - start) + " ns");
    }
}
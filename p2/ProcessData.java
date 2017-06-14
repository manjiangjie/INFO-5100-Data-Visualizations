import java.io.*;
import java.util.*;
import java.util.Comparator;

/**
 * Created by xinxiuyan on 17/4/20.
 */
public class ProcessData {
    public static void makeStationMap(HashMap<String, Integer> emptyMap) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("src/station.csv"));
        String line = null;
        while((line = br.readLine()) != null) {
            // 1: station name, 5: city name
            String city_name = line.split(",")[5];
            String station_name = line.split(",")[1];

            if(city_name.equals("San Francisco")){
                emptyMap.put(station_name, 0);
            }
        }
    }
    public static void calculateFrequency(HashMap<String, Integer> startMap, HashMap<String, Integer> endMap) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("src/trip.csv"));
        String line = null;
        while((line = br.readLine()) != null) {
            String date = line.split(",")[2];

            if(date.contains("2014")) {
                String start_station = line.split(",")[3];
                String end_station = line.split(",")[6];
                if(startMap.containsKey(start_station)){
                    startMap.put(start_station, startMap.get(start_station) + 1);
                }
                if(endMap.containsKey(end_station)){
                    endMap.put(end_station, endMap.get(end_station) + 1);
                }
            }
        }
    }
    public static void sortAndWrite(HashMap<String, Integer> map, String fileName) throws IOException {
        Object[] a = map.entrySet().toArray();
        Arrays.sort(a, new Comparator() {
            public int compare(Object o1, Object o2) {
                return ((Map.Entry<String, Integer>) o2).getValue()
                        .compareTo(((Map.Entry<String, Integer>) o1).getValue());
            }
        });

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fileName)));
        for (Object e : a) {
            String line = ((Map.Entry<String, Integer>) e).getKey() + ","
                    + ((Map.Entry<String, Integer>) e).getValue();

            System.out.println(line);
            bw.write(line + "\n");

        }
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        // key: station name, value: number of appearance
        HashMap<String, Integer> startMap = new HashMap<>();
        HashMap<String, Integer> endMap = new HashMap<>();
        makeStationMap(startMap);
        makeStationMap(endMap);
        calculateFrequency(startMap, endMap);
        sortAndWrite(startMap, "SortedStartMap.csv");
        sortAndWrite(endMap, "SortedEndMap.csv");
    }
}

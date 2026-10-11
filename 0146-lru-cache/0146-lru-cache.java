import java.util.HashMap;
import java.util.LinkedHashSet;

class LRUCache {
    private final int capacity;
    private final HashMap<Integer, Integer> map;
    private final LinkedHashSet<Integer> order;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.order = new LinkedHashSet<>();
    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        order.remove(key);
        order.add(key);
        return map.get(key);
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            map.put(key, value);
            order.remove(key);
            order.add(key);
        } else {
            if (map.size() >= capacity) {
                int lru = order.iterator().next();
                order.remove(lru);
                map.remove(lru);
            }
            map.put(key, value);
            order.add(key);
        }
    }
}
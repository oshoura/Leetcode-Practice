import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class LRUCache {

    private Map<Integer, Integer> map;
    private List<Integer> keyStack;
    private int capacity;

    public LRUCache(int capacity) throws IllegalArgumentException {
        if (capacity > 0) {
            this.capacity = capacity;
        } else {
            throw new IllegalArgumentException("capacity must be positive");
        }
        this.map = new HashMap<Integer, Integer>();
        this.keyStack = new ArrayList<>();
    }

    public int get(int key) {
        int indexInStack = this.keyStack.indexOf(key);
        if (indexInStack == -1) { // couldn't find it
            return indexInStack;
        }
        // put key stack at the top of the stack and remove old occurance of it
        this.keyStack.remove(indexInStack);
        this.keyStack.add(key);
        return map.get(key);
    }

    public void put(int key, int value) {
        // check if it already exists
        if (this.map.get(key) != null) {
            this.map.put(key, value);
            // simulate getting the keyVal to put it at the top of the stack
            this.get(key);
            return;
        }
        int len = keyStack.size();
        if (len >= capacity) {
            // find the least used cache
            int leasUsed = this.keyStack.get(0);
            // remove old from map then stack
            this.map.remove(leasUsed);
            this.keyStack.remove(0);
        }
        // add new key to map and stack
        this.map.put(key, value);
        this.keyStack.add(key);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
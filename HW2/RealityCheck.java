import java.util.HashMap;
import java.util.Map;

public class RealityCheck {
    public Map<Integer, Integer> m_map;
    public Map<Integer, Integer> s_map;

    public RealityCheck(){
        m_map = new HashMap<>();
        s_map = new HashMap<>();
    }

    public int M(int n) {
        if (n <= 1) return 0;

        if (m_map.containsKey(n)) return m_map.get(n);

        m_map.put(n, M((int)Math.floor((double)n/2)) + M((int)Math.ceil((double)n/2)) + n - 1);
        return m_map.get(n);
    }

    public int S(int n) {
        if (n < 100) return M(n);

        if (s_map.containsKey(n)) return s_map.get(n);

        s_map.put(n, Math.min(M(n), (8 * (int)Math.ceil(n/5.0)) + S((int)Math.ceil(n/5.0)) + S((int)Math.floor(7*n/10.0))));
    
        return s_map.get(n);
    }

    public int dumbsearch(int start){
        while (3 * S(start) > 2 * M(start)){
            start++;
        }
        return start;
    }

    public static void main(String[] args) {
        RealityCheck rc = new RealityCheck();

        int n0 = 324;
        System.out.println(rc.S(n0));
        System.out.println(rc.M(n0));

        System.err.println(rc.dumbsearch(100));
    }
}

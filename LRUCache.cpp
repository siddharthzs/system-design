static const auto fast = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    return 0;
} ();

class LRUCache {
private:
    struct ListNode {
        int key;
        int value;
        ListNode* prev;
        ListNode* next;
        
        ListNode(int key, int value) : key{key}, value{value}, prev{nullptr}, next{nullptr} {}
    };
    
    int capacity;
    ListNode* head;
    ListNode* tail;
    std::unordered_map<int, ListNode*> cache;
    
    void moveFirst(ListNode* node) {
        if (!node) return;
        if (node == head) return;
        if (node == tail) {
            tail->next = head;
            head->prev = tail;
            
            tail = tail->prev;
            head = head->prev;
            
            tail->next = nullptr;
            head->prev = nullptr;
            return;
        }
        
        node->prev->next = node->next;
        node->next->prev = node->prev;
        node->prev = nullptr;
        node->next = head;
        head->prev = node;
        head = node;
    }
    
    void addFirst(ListNode* node) {
        if (!head) {
            head = node;
            tail = head;
            return;
        }
        
        node->next = head;
        head->prev = node;
        head = node;
    }
    
public:
    LRUCache(int capacity) : capacity{capacity}, head{nullptr}, tail{nullptr} {}
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        
        moveFirst(it->second);
        return it->second->value;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            it->second->value = value;
            moveFirst(it->second);
            return;
        }
        
        if (cache.size() < capacity) {
            auto node = new ListNode(key, value);
            addFirst(node);
            cache.insert({key, node});
            return;
        }
        
        cache.erase(tail->key);
        cache.insert({key, tail});
        tail->key = key;
        tail->value = value;
        moveFirst(tail);
    }
};











class LRUCache(OrderedDict):

  def __init__(self, capacity: int):
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key in self:
      self.move_to_end(key)
      return self[key]
    return -1

  def put(self, key: int, value: int) -> None:
    self[key] = value
    self.move_to_end(key)
    if len(self) > self.capacity:
      self.popitem(last=False)


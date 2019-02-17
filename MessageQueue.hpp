#ifndef _MESSAGEQUEUE
// 暂存文件
#include <Arduino.h>

template <typename T>
class Queue {
	class Node {
	public:
		T item;
		Node* next;

		Node() {
			next = NULL;
		}

		~Node() {
			next = NULL;
		}
	};
private:
	Node* tail;
	int len;

public:
  Node* head;
	Queue() {
		head = NULL;
		tail = NULL;
		len = 0;
	}

	void clear() {
		for (Node* node = head; node != NULL; node = head) {
			head = node->next;
			delete node;
		}
		len = 0;
	}

	~Queue() {
		clear();
	}

	// Returns false if memory is full, otherwise true
	bool push(T item) {
		Node* node = new Node;
		if (node == NULL) {
			return false;
		}

		node->item = item;

		if (head == NULL) {
			head = node;
			tail = node;
			len = 1;
			return true;
		}

		tail->next = node;
		tail = node;
		len ++;
		return true;
	}

	/*
		Pop the front of the queue.
		Because exceptions are not
		usually implemented for
		microcontrollers, if queue
		is empty, a dummy item is
		returned.
	*/

	T pop() {
		if (head == NULL) {
			return T();
		}

		Node* node = head;
		head = node->next;
		T item = node->item;
		delete node;
		len --;
		node = NULL;

		if (head == NULL) {
			tail = NULL;
		}

		return item;
	}

	bool remove(T item) {
		if (head == NULL || !contains(item)) {
			return false;
		}

		Node *node = head;
		if (node->item == item) {
			if (node->next == NULL) clear();
			else {
				head = node->next;
				delete node;
			}
			return true;
		}

		while(node->next != NULL) {
			if (node->next->item == item) {
				if (node->next->next == NULL) {
					tail = node;
					delete node->next;
				} else {
					Node *tmp = node->next;
					node->next = node->next->next;
					delete tmp;
				}
				return true;
			}
			node = node->next;
		}
	}

	bool isEmpty() {
		return len == 0;
	}

	/*
		Get the front of the queue.
		Because exceptions are not
		usually implemented for
		microcontrollers, if queue
		is empty, a dummy item is
		returned.
	*/
	T front() {
		if (head == NULL) {
			return T();
		}

		T item = head->item;

		return item;
	}

	T end() {
		if (tail == NULL) {
			return T();
		}

		T item = tail->item;

		return item;
	}

  bool contains(T item) {
    Node *node = head;
    while(node != NULL) {
      if (item == node->item) return true;
      node = node->next;
    }
    return false;
  }

	int length() {return len;}

	const Queue<T>& operator= (const Queue<T>& queue) {
		if (&queue != NULL) {
			clear();
			Node *node = queue.head;
			while (node != NULL) {
				push(node->item);
				node = node->next;
			}
		}
		return *this;
	}

};


const Queue<String> split(String str, String words) {
  Queue<String> tmp;
  int index = str.indexOf(words);
  int cnt = 0;
  while (index != -1) {
    String tStr = str.substring(0, index);
    Serial.println(tStr);
    if (!tmp.push(tStr)) {
      return tmp;
    }
    cnt ++;
    str = str.substring(index+1, str.length());
    index = str.indexOf(words);
  }
  if (!tmp.push(str)) {
      return tmp;
  }
  Serial.println(str);
  return tmp;
}

class MessageQueue {
  class Message {
  private:
    Queue<String> strQueue;
  public:
    String id;
    String body;
    Message() {id = "";body = "";}
    Message(String msg) {
      strQueue = split(msg, "*");
      if (strQueue.length() == 2) {
        id = strQueue.pop();
        body = strQueue.pop();
      }
    }
    bool operator== (const Message& msg) {
			if (msg.id == this->id) return true;
			return false;
		}
    bool operator== (const String _id) {
			if (_id == this->id) return true;
			return false;
		}
  };
private:
  int capacity;
  Queue<Message> queue;
public:
  MessageQueue() {
    capacity = 10;
  }

  bool push(String str) {
    if (!queue.push(Message(str))) {
      return false;
    }
    if (queue.length() >= capacity) {
      queue.pop();
    }
    return true;
  }

  Message pop() {
    return queue.pop();
  }

  Message end() {
    return queue.end();
  }

  Message front() {
    return queue.front();
  }

  int length() {return queue.length();}

};

#endif

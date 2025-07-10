#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

struct Node
{
    Node *links[26];
    bool isEnd = false;

    bool containsKey(char ch)
    {
        return links[ch - 'a'] != NULL;
    }

    void put(char ch, Node *node)
    {
        links[ch - 'a'] = node;
    }

    Node *get(char ch)
    {
        return links[ch - 'a'];
    }

    void setEnd()
    {
        isEnd = true;
    }

    bool isEndNode()
    {
        return isEnd;
    }
};

class Trie
{
private:
    Node *root;

public:
    Trie()
    {
        root = new Node();
    }

    void insert(string word)
    {
        Node *node = root;
        for (char ch : word)
        {
            if (!node->containsKey(ch))
            {
                node->put(ch, new Node());
            }
            node = node->get(ch);
        }
        node->setEnd();
    }

    bool checkAllPrefixes(string word)
    {
        Node *node = root;
        for (char ch : word)
        {
            node = node->get(ch);
            if (!node->isEndNode())
            {
                return false;
            }
        }
        return true;
    }
};

string completeString(int n, vector<string> &a)
{
    Trie trie;
    for (auto &word : a)
    {
        trie.insert(word);
    }

    string longest = "";
    for (auto &word : a)
    {
        if (trie.checkAllPrefixes(word))
        {
            if (word.length() > longest.length() ||
                (word.length() == longest.length() && word < longest))
            {
                longest = word;
            }
        }
    }

    if (longest == "")
        return "None";
    return longest;
}

int main()
{
    vector<string> words = {"a", "ap", "app", "appl", "apple", "apply"};
    cout << completeString(words.size(), words) << endl;
    return 0;
}

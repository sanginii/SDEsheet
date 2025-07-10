#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
struct Node
{
    Node *link[2];
    bool containsKey(int bit)
    {
        return (link[bit] != NULL);
    }
    void put(Node *node, int bit)
    {
        link[bit] = node;
    }
    Node *getKey(int bit)
    {
        return link[bit];
    }
};
class Trie
{
    Node *root;

public:
    Trie()
    {
        root = new Node();
    }
    void insert(int num)
    {
        Node *node = root;
        for (int i = 31; i >= 0; i--)
        {
            int bit = (num >> i) & 1;
            if (!node->containsKey(bit))
            {
                node->put(new Node(), bit);
            }
            node = node->getKey(bit);
        }
    }
    int getMax(int x)
    {
        int max = 0;
        Node *node = root;
        for (int i = 31; i >= 0; i--)
        {
            int bit = (x >> i) & 1;
            if (node->containsKey(1 - bit))
            {
                max = max | (1 << i);
                node = node->getKey(1 - bit);
            }
            else
            {
                node = node->getKey(bit);
            }
        }
        return max;
    }
};

class Solution
{
public:
    vector<int> maximizeXor(vector<int> &nums, vector<vector<int>> &queries)
    {
        sort(nums.begin(), nums.end());
        vector<pair<int, pair<int, int>>> oq; // pair is like tuple
        int q = queries.size();
        for (int i = 0; i < q; i++)
        {
            oq.push_back({queries[i][1], {queries[i][0], i}}); // push_back is insert
        }
        sort(oq.begin(), oq.end());
        vector<int> ans(q, 0); // size and initialize with 0
        Trie trie;
        int j = 0;
        int n = nums.size();
        for (int i = 0; i < q; i++)
        {
            int a = oq[i].first;
            int x = oq[i].second.first;
            int qind = oq[i].second.second;
            while (j < n && nums[j] <= a)
            {
                trie.insert(nums[j]);
                j++;
            }
            if (j == 0)
            {
                ans[qind] = -1;
            }
            else
            {
                ans[qind] = trie.getMax(x);
            }
        }
        return ans;
    }
};
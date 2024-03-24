#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(const vector<int> &numbers, int target, int index, int values) {
    if (index == numbers.size()) {
        if (values == target)
            answer++;
        return;
    }
    
    dfs(numbers, target, index + 1, values + numbers[index]);
    dfs(numbers, target, index + 1, values - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}
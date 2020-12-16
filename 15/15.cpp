#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <vector>

std::vector<int> parse_input() {
  std::vector<int> v;
  do {
    int x;
    assert(scanf("%d", &x) == 1);
    v.push_back(x);

    char ch{};
    if (scanf("%c", &ch) != 1 || ch != ',') {
      break;
    }
  } while (true);
  return v;
}

int main(int argc, char **argv) {
  assert(argc == 2);
  const int req_pos = atoi(argv[1]);
  const auto v = parse_input();

  std::vector<int> last_occur(req_pos + 1, 0);
  int cur_pos = 0;

  auto add_element = [&](int val) {
    ++cur_pos;
    int next = (last_occur[val] == 0 ? 0 : cur_pos - last_occur[val]);
    last_occur[val] = cur_pos;
    return next;
  };

  int next{-1};
  for (auto x : v) {
    next = add_element(x);
  }
  while (cur_pos != req_pos - 1) {
    next = add_element(next);
  }
  printf("%d\n", next);

  return 0;
}


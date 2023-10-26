// Example of ignore whitespace scorer
#include <bits/stdc++.h>
using namespace std;

ifstream inp;
ifstream out;
ifstream con;

void ac(string reason="") {
  cout << "AC\n";
  if (reason != "") {
    cout << reason << '\n';
  }
  exit(0);
}

void wa(string reason="") {
  cout << "WA\n";
  if (reason != "") {
    cout << reason << '\n';
  }
  exit(0);
}

void ok(double points, string reason="") {
  cout << "OK\n";
  cout << points;
  if (reason != "") {
    cout << " " << reason << '\n';
  }
  exit(0);
}

void registerScorer(int argc, char* argv[]) {
  if (argc != 4) {
    cout << "Must be run with arguments [input-file] [output-file] [contestant-output]\n";
    exit(0);
  }

  inp = ifstream(argv[1]);
  out = ifstream(argv[2]);
  con = ifstream(argv[3]);
}

void TLCassert(bool ok, string reason="") {
  if (!ok) {
    wa(reason);
  }
}

template<class T> inline void readStream(ifstream &ifs, T &t) { if (!(ifs >> t)) wa(); }
template<class T> inline void readStream(stringstream &ifs, T &t) { if (!(ifs >> t)) wa(); }

void eof() {
  string dummy;
  if (con >> dummy) wa("Extra output");
}

void adjudicate() {
  string juryOut, conOut;
  while (out >> juryOut) {
    readStream(con, conOut);
    TLCassert(juryOut == conOut);
  }
  eof();
  // ok(100/0);
  ac();
}

int main(int argc, char* argv[]) {
  registerScorer(argc, argv);
  adjudicate();
}
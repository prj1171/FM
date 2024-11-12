#include <bits/stdc++.h>
using namespace std;

vector<float> readCSV(string filename) {
    vector<float> numbers;
    ifstream file(filename);
    
    if (!file.is_open()) {
        cout << "Error opening input file!" << endl;
        return numbers;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string value;

        while (getline(ss, value, ',')) {
            value.erase(0, value.find_first_not_of(" \t\r\n"));
            value.erase(value.find_last_not_of(" \t\r\n") + 1);
            
            try {
                numbers.push_back(stof(value));
            } catch (const exception& e) {
                cout << "Error converting value: " << value << endl;
            }
        }
    }
    file.close();
    return numbers;
}

bool writeCSV(const vector<float>& values, const string& filename) {
    ofstream file(filename);
    if (!file.is_open()) {
        cout << "Error opening output file!" << endl;
        return false;
    }
    
    file << fixed << setprecision(4);
    
    for (const auto& value : values) {
        file << value << "\n";
    }
    
    file.close();
    return true;
}

int main() {
    string inputFilename = "house_data.csv";
    vector<float> values = readCSV(inputFilename);
    
    if (values.empty()) {
        cout << "No values were read from the file!" << endl;
        return 1;
    }

    sort(values.begin(), values.end());

    float n = values.size();
    float minvalue = values[0];
    float maxvalue = values[n-1];
    float newmin, newmax;
    
    cout << "Enter the new minimum: ";
    cin >> newmin;
    cout << "Enter the new maximum: ";
    cin >> newmax;

    if (newmin >= newmax) {
        cout << "Error: New minimum must be less than new maximum!" << endl;
        return 1;
    }

    vector<float> normalizedvalues;
    float range = newmax - newmin;
    float oldrange = maxvalue - minvalue;

    if (oldrange == 0) {
        cout << "Error: All input values are the same!" << endl;
        return 1;
    }

    for (int i = 0; i < n; i++) {
        float normalizedvalue = newmin + range * ((values[i] - minvalue) / oldrange);
        normalizedvalues.push_back(normalizedvalue);
    }

    string outputFilename = "normalized_data.csv";
    if (writeCSV(normalizedvalues, outputFilename)) {
        cout << "Normalized values have been written to " << outputFilename << endl;
        cout << "Number of values processed: " << normalizedvalues.size() << endl;
    } else {
        cout << "Failed to write output file!" << endl;
        return 1;
    }

    return 0;
}
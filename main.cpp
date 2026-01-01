#include <iostream>
#include <vector>

// A simple function to calculate the average price
double calculate_average(const std::vector<double>& prices) {
    double sum = 0;
    // BUG: <= causes us to read one step PAST the end of the vector
    for (size_t i = 0; i <= prices.size(); ++i) {
        sum += prices[i];
    }
    return sum / prices.size();
}

int main() {
    std::vector<double> market_data = {100.5, 101.2, 100.8, 102.1};

    std::cout << "Processing " << market_data.size() << " orders..." << std::endl;

    double avg = calculate_average(market_data);

    std::cout << "Average Price: " << avg << std::endl;
    return 0;
}

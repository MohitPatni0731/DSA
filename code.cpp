#include <iostream>
#include <vector>
#include <string>
#include <map>

/* Alert Examples:
     name=Alert_1; condition="avg(MemUtil)>80"; splitby=host
     name=Alert_2; condition="avg(CpuUtil)>85"; splitby=app
     name=Alert_3; condition="avg(CpuUtil)>90"; splitby=host

  Alerts will be combined into groups for efficient evaluation (every minute) based on 
  Group Key (i.e., splitby). Group examples
        key=host,   alerts={Alert_1, Alert_3};
        key=app,    alerts={Alert_2};

  Requirements: 
    Understand the existing data structure and code; 
    Answer Questions 1-4 by adding additional data structure and code.
*/
class Alert {
public:
    Alert(const std::string& name0, const std::string& condition0, const std::string& splitby0) :
            name(name0), condition(condition0), splitby(splitby0) {}
    std::string getGroupKey() const { return splitby; }
private:
    std::string name, condition, splitby;
};
typedef std::vector<Alert> Alerts;

class AlertGroup {
public:
    std::string key;
    Alerts alerts;
};

// singleton pattern
class AlertManager {
private:
    AlertManager() {}   // private constructor
public:
    static AlertManager& instance() {
        static AlertManager instance;
        return instance;
    }

public:
    // Question 1b: Implement the function to retrieve alerts with groupKey
    void getAlertsPerGroup(const std::string& groupKey, Alerts& output_alerts) {
      // Check karenge ki groupKey _alertGroups main hai kya aur agar hai toh ouput_alerts main usko add kar denge ni toh output_alerts khali pada rahega 
        if (_alertGroups.contains(groupKey)) {
    output_alerts = _alertGroups[groupKey];
      }
    }

public:
    // reads alerts from disk and populates internal data structure.
    void reloadAlerts() {
        Alerts alerts;
        _readAlerts(alerts);
        _groupAlerts(alerts);
    }

private:
    // reads alerts from disk
    void _readAlerts(Alerts& alerts) {
        // emulated implementation
        Alert alert1("Alert_1", "avg(CpuUtil)>80", "host");
        Alert alert2("Alert_2", "avg(CpuUtil)>85", "app");
        Alert alert3("Alert_3", "avg(CpuUtil)>90", "host");
        alerts.push_back(alert1);
        alerts.push_back(alert2);
        alerts.push_back(alert3);
    }


    // Question 2: Implement the function to group alerts into _alertGroups based on Alert::getGroupKey()
    void _groupAlerts(const Alerts& alerts) {
      // isme alertGroups ko pehle khaali karke phir ek loop chalayennge alerts pe phir key leke usko correct group main daal denge
        _alertGroups.clear();  

      for (const Alert& alert : alerts) {  
          std::string key = alert.getGroupKey();  
          _alertGroups[key].push_back(alert);  
      }
    }

private:
    // Question 1a: Define a data structure for _alertGroups so getAlertsPerGroup can be efficient
    // Vector ko use kar sakte hai wahi sahi rahega kyoki usme mapping kar sakte hai group key ko to list of alerts
    std::map<std::string, Alerts> _alertGroups;
};

int main() {
    AlertManager& mgr = AlertManager::instance();
    mgr.reloadAlerts();

    // Q: how to unit test the functions you implemented?
    Alerts alerts1;
    std::string groupKey = "host";
    mgr.getAlertsPerGroup(groupKey, alerts1);
    std::cout << alerts1.size() << std::endl;
}

// Question 3: How to extend AlertManager so it can offer an additional function efficiently
//    void getAlert(const std::string& name, Alert &alert);

// Question 4: (if not done in Question 3) How to eliminate duplicate copies of alerts?

// Question 5: How to make it thread safe, assuming getAlertsPerGroup() and reloadAlerts() can be called by different threads?

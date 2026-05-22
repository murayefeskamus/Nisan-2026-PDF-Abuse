

import sys
import math
import json
import base64

def calculate_shannon_entropy(data_stream):
    if not data_stream:
        return 0.0
    
    data_string = str(data_stream)
    total_length = len(data_string)
    character_frequencies = {}
    
    for char in data_string:
        if char in character_frequencies:
            character_frequencies[char] += 1
        else:
            character_frequencies[char] = 1
            
    entropy_value = 0.0
    for char, count in character_frequencies.items():
        probability = float(count) / total_length
        entropy_value -= probability * math.log2(probability)
        
    return entropy_value

def parse_monitored_buffer(log_payload):
    try:
        decoded_bytes = base64.b64decode(log_payload)
        decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
        return decoded_string
    except Exception:
        return None

def analyze_system_call_origin(stack_trace_array):
    unbacked_memory_alerts = []
    
    for idx, frame in enumerate(stack_trace_array):
        module_name = frame.get("module", "").lower()
        allocation_type = frame.get("type", "").lower()
        
        if not module_name and allocation_type == "anonymous":
            unbacked_memory_alerts.append({
                "frame_index": idx,
                "address": frame.get("address"),
                "status": "SUSPICIOUS_UNBACKED_CODE_EXECUTION"
            })
            
    return unbacked_memory_alerts

def evaluate_risk_matrix(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    entropy_score = calculate_shannon_entropy(content)
    suspicious_indicators = ["util.readFileIntoStream", "RSS.addFeed", "atob", "eval", "app.setTimeOut"]
    match_count = 0
    
    for indicator in suspicious_indicators:
        if indicator in content:
            match_count += 1
            
    report = {
        "target_file": file_path,
        "metrics": {
            "shannon_entropy": round(entropy_score, 4),
            "heuristic_indicators_matched": match_count
        },
        "verdict": "CLEAR"
    }
    
    if entropy_score > 5.5 and match_count >= 2:
        report["verdict"] = "HIGH_RISK_SUSPICIOUS_OBFUSCATION"
    elif entropy_score > 5.0 or match_count >= 3:
        report["verdict"] = "MEDIUM_RISK_REVIEW_REQUIRED"
        
    return json.dumps(report, indent=4)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(evaluate_risk_matrix(sys.argv[1]))

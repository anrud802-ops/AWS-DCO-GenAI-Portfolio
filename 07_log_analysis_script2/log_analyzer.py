import glob
import os
import re

def analyze_logs():
    # Regular expression to match the server name token (e.g. server01, server02)
    server_pattern = re.compile(r'^server\d+$')
    
    # Dictionary to store the counts for each server
    # Format: {server_name: {'crc_error': count, 'link_down': count}}
    stats = {}
    
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob('server*.log'))
    
    if not log_files:
        print("No server*.log files found in the current directory.")
        return

    for path in log_files:
        filename_base = os.path.splitext(os.path.basename(path))[0]
        stats[filename_base] = {'crc_error': 0, 'link_down': 0}
        
        # Read and group lines into multi-line log entries
        entries = []
        current_entry = []
        
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                
                # Check if this is a continuation line of a multi-line log entry.
                # Continuation lines start with spaces, tabs, or '->'
                is_continuation = line.startswith(' ') or line.startswith('\t') or stripped.startswith('->')
                
                if is_continuation and current_entry:
                    current_entry.append(line)
                else:
                    if current_entry:
                        entries.append(''.join(current_entry))
                    current_entry = [line]
            
            if current_entry:
                entries.append(''.join(current_entry))
                
        # Analyze each grouped entry
        for entry in entries:
            first_line = entry.splitlines()[0]
            tokens = first_line.split()
            level = None
            
            # Find the log level (right after the server name token)
            for i, token in enumerate(tokens):
                if server_pattern.match(token):
                    if i + 1 < len(tokens):
                        level = tokens[i + 1]
                    break
            
            # Count errors case-insensitively only for entries with log level 'ERROR'
            if level and level.upper() == 'ERROR':
                entry_lower = entry.lower()
                if 'crc error' in entry_lower:
                    stats[filename_base]['crc_error'] += 1
                elif 'link down' in entry_lower:
                    stats[filename_base]['link_down'] += 1

    # Print the formatted result table
    print("=" * 50)
    print(" Server Log Analysis Results (Grouped Multi-line)")
    print("=" * 50)
    print(f" {'Server':<12} | {'CRC Error':^11} | {'Link Down':^11}")
    print("-" * 50)
    
    total_crc = 0
    total_ld = 0
    
    for server, counts in stats.items():
        crc = counts['crc_error']
        ld = counts['link_down']
        total_crc += crc
        total_ld += ld
        print(f" {server:<12} | {crc:>11} | {ld:>11}")
        
    print("-" * 50)
    print(f" {'Total':<12} | {total_crc:>11} | {total_ld:>11}")
    print("=" * 50)

if __name__ == '__main__':
    analyze_logs()

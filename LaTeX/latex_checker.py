#!/usr/bin/env python3
"""
LaTeX Syntax Checker for presentation_aircraft_analysis.tex
Checks for common LaTeX compilation issues
"""

import re
import os

def check_latex_file(filepath):
    """Check LaTeX file for common syntax issues"""
    print(f"Checking LaTeX file: {filepath}")
    print("=" * 50)
    
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} does not exist!")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    warnings = []
    
    # Check for unmatched braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        issues.append(f"Unmatched braces: {open_braces} opening, {close_braces} closing")
    
    # Check for unmatched environments
    begin_count = len(re.findall(r'\\begin\{', content))
    end_count = len(re.findall(r'\\end\{', content))
    if begin_count != end_count:
        issues.append(f"Unmatched environments: {begin_count} \\begin, {end_count} \\end")
    
    # Check for missing \end{document}
    if not re.search(r'\\end\{document\}', content):
        issues.append("Missing \\end{document}")
    
    # Check for image files
    image_refs = re.findall(r'\\includegraphics[^{]*\{([^}]+)\}', content)
    base_dir = os.path.dirname(filepath)
    for img_path in image_refs:
        # Convert relative path to absolute
        if img_path.startswith('../'):
            img_full_path = os.path.join(base_dir, img_path)
        else:
            img_full_path = os.path.join(base_dir, img_path)
        
        if not os.path.exists(img_full_path):
            issues.append(f"Missing image file: {img_path} (resolved: {img_full_path})")
    
    # Check for unescaped special characters (excluding proper escapes)
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('%'):
            continue
        
        # Check for unescaped underscores (not in \texttt{} or already escaped)
        if re.search(r'(?<!\\)_(?![}])', line) and '\\texttt{' not in line:
            warnings.append(f"Line {i}: Possible unescaped underscore: {line.strip()}")
        
        # Check for unescaped ampersands (not in tabular)
        if re.search(r'(?<!\\)&(?![}])', line) and '\\begin{tabular}' not in content[max(0, content.find(line) - 200):content.find(line) + 200]:
            warnings.append(f"Line {i}: Possible unescaped ampersand: {line.strip()}")
    
    # Report results
    if not issues and not warnings:
        print("✅ No obvious LaTeX syntax issues found!")
        return True
    
    if issues:
        print("🚨 CRITICAL ISSUES:")
        for issue in issues:
            print(f"   - {issue}")
    
    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   - {warning}")
    
    return len(issues) == 0

def main():
    latex_file = "/Users/aminborqal/Documents/Projects/Python/Statistical-Learning/StatisticalLearningProject/LaTeX/presentation_aircraft_analysis.tex"
    
    is_valid = check_latex_file(latex_file)
    
    print("\n" + "=" * 50)
    if is_valid:
        print("✅ File appears to be syntactically correct!")
        print("If compilation fails, it might be due to:")
        print("   - Missing LaTeX packages")
        print("   - LaTeX distribution issues")
        print("   - Image path problems")
    else:
        print("❌ File has syntax issues that need to be fixed!")
    
    # Additional check: verify image paths
    print("\n📁 Checking image references...")
    base_dir = os.path.dirname(latex_file)
    with open(latex_file, 'r') as f:
        content = f.read()
    
    image_refs = re.findall(r'\\includegraphics[^{]*\{([^}]+)\}', content)
    for img_path in image_refs:
        if img_path.startswith('../'):
            img_full_path = os.path.join(base_dir, img_path)
        else:
            img_full_path = os.path.join(base_dir, img_path)
        
        if os.path.exists(img_full_path):
            print(f"   ✅ {img_path}")
        else:
            print(f"   ❌ {img_path} -> {img_full_path}")

if __name__ == "__main__":
    main()

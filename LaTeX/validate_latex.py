#!/usr/bin/env python3
"""
LaTeX Validation Script - Verifica emoji e caratteri speciali
"""

import re

def check_latex_issues(filepath):
    """Controlla problemi LaTeX comuni"""
    print(f"🔍 Controllo file: {filepath}")
    print("=" * 60)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    issues = []
    
    for i, line in enumerate(lines, 1):
        # Controllo emoji/caratteri Unicode problematici
        if re.search(r'[📊🔧🚀✈️⬇️⛽🌍📏🦅⚖️📈📉🛫🛬]', line):
            issues.append(f"Linea {i}: Emoji trovata - {line.strip()}")
        
        # Controllo parentesi non bilanciate
        open_paren = line.count('(')
        close_paren = line.count(')')
        if open_paren != close_paren and ('item[' in line):
            issues.append(f"Linea {i}: Parentesi non bilanciate - {line.strip()}")
        
        # Controllo caratteri speciali problematici
        if re.search(r'[""''–—]', line):
            issues.append(f"Linea {i}: Caratteri speciali trovati - {line.strip()}")
    
    # Controllo bilanciamento generale
    open_braces = content.count('{')
    close_braces = content.count('}')
    begin_count = len(re.findall(r'\\begin\{', content))
    end_count = len(re.findall(r'\\end\{', content))
    
    print("📊 RISULTATI CONTROLLO:")
    print(f"   Parentesi graffe: {open_braces} aperte, {close_braces} chiuse")
    print(f"   Ambienti: {begin_count} \\begin, {end_count} \\end")
    
    if issues:
        print("\n❌ PROBLEMI TROVATI:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    else:
        print("\n✅ NESSUN PROBLEMA CRITICO TROVATO!")
        print("   - Nessuna emoji problematica")
        print("   - Sintassi LaTeX pulita")
        print("   - Bilanciamento corretto")
        return True

if __name__ == "__main__":
    file_path = "/Users/aminborqal/Documents/Projects/Python/Statistical-Learning/StatisticalLearningProject/LaTeX/presentation_aircraft_analysis.tex"
    
    try:
        is_clean = check_latex_issues(file_path)
        
        print("\n" + "=" * 60)
        if is_clean:
            print("🎉 FILE PRONTO PER LA COMPILAZIONE!")
            print("   Ora dovresti essere in grado di compilare con:")
            print("   pdflatex presentation_aircraft_analysis.tex")
        else:
            print("⚠️  CORREZIONI NECESSARIE PRIMA DELLA COMPILAZIONE")
            
    except FileNotFoundError:
        print(f"❌ File non trovato: {file_path}")
    except Exception as e:
        print(f"❌ Errore: {e}")

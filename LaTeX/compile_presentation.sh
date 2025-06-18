#!/bin/bash
# LaTeX Compilation Script for presentation_aircraft_analysis.tex
# Run with: bash compile_presentation.sh

echo "🔨 Compiling Aircraft Price Analysis Presentation..."
echo "=================================================="

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "❌ Error: pdflatex not found!"
    echo "Please install LaTeX first. See install_guide.sh"
    exit 1
fi

# Set the presentation file
PRESENTATION="presentation_aircraft_analysis.tex"

if [ ! -f "$PRESENTATION" ]; then
    echo "❌ Error: $PRESENTATION not found!"
    exit 1
fi

echo "📄 File: $PRESENTATION"
echo "📁 Working directory: $(pwd)"

# Check if images directory exists
if [ ! -d "../images" ]; then
    echo "⚠️  Warning: ../images directory not found!"
    echo "Expected images:"
    grep "includegraphics" "$PRESENTATION" | sed 's/.*{\([^}]*\)}.*/  - \1/'
fi

echo ""
echo "🔄 Running first pdflatex pass..."
pdflatex -interaction=nonstopmode "$PRESENTATION"

if [ $? -eq 0 ]; then
    echo "✅ First pass completed successfully!"
    
    echo "🔄 Running second pdflatex pass (for references)..."
    pdflatex -interaction=nonstopmode "$PRESENTATION"
    
    if [ $? -eq 0 ]; then
        echo "✅ Compilation successful!"
        echo "📄 Output: presentation_aircraft_analysis.pdf"
        
        # Show file size
        if [ -f "presentation_aircraft_analysis.pdf" ]; then
            SIZE=$(ls -lh presentation_aircraft_analysis.pdf | awk '{print $5}')
            echo "📊 File size: $SIZE"
        fi
        
        # Clean up auxiliary files
        echo "🧹 Cleaning up auxiliary files..."
        rm -f *.aux *.log *.nav *.out *.snm *.toc *.synctex.gz
        echo "✨ Done!"
    else
        echo "❌ Second pass failed!"
        echo "Check the log file for errors: presentation_aircraft_analysis.log"
    fi
else
    echo "❌ First pass failed!"
    echo "Check the log file for errors: presentation_aircraft_analysis.log"
    
    # Show last few lines of log file if it exists
    if [ -f "presentation_aircraft_analysis.log" ]; then
        echo ""
        echo "📋 Last 10 lines of log file:"
        tail -10 "presentation_aircraft_analysis.log"
    fi
fi

echo ""
echo "=== Compilation Summary ==="
if [ -f "presentation_aircraft_analysis.pdf" ]; then
    echo "Status: ✅ SUCCESS"
    echo "Output: presentation_aircraft_analysis.pdf"
else
    echo "Status: ❌ FAILED"
    echo "Check presentation_aircraft_analysis.log for details"
fi

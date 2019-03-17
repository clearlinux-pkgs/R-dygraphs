#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dygraphs
Version  : 1.1.1.6
Release  : 17
URL      : https://cran.r-project.org/src/contrib/dygraphs_1.1.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dygraphs_1.1.1.6.tar.gz
Summary  : Interface to 'Dygraphs' Interactive Time Series Charting Library
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: R-htmlwidgets
Requires: R-rmarkdown
Requires: R-xts
Requires: R-zoo
BuildRequires : R-htmlwidgets
BuildRequires : R-rmarkdown
BuildRequires : R-xts
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
(a copy of which is included in the package). Provides rich facilities
    for charting time-series data in R, including highly configurable
    series- and axis-display and interactive features like zoom/pan and
    series/point highlighting.

%prep
%setup -q -c -n dygraphs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531363012

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531363012
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dygraphs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dygraphs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dygraphs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library dygraphs|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dygraphs/COPYING
/usr/lib64/R/library/dygraphs/DESCRIPTION
/usr/lib64/R/library/dygraphs/INDEX
/usr/lib64/R/library/dygraphs/LICENSE
/usr/lib64/R/library/dygraphs/Meta/Rd.rds
/usr/lib64/R/library/dygraphs/Meta/features.rds
/usr/lib64/R/library/dygraphs/Meta/hsearch.rds
/usr/lib64/R/library/dygraphs/Meta/links.rds
/usr/lib64/R/library/dygraphs/Meta/nsInfo.rds
/usr/lib64/R/library/dygraphs/Meta/package.rds
/usr/lib64/R/library/dygraphs/NAMESPACE
/usr/lib64/R/library/dygraphs/NEWS
/usr/lib64/R/library/dygraphs/NOTICE
/usr/lib64/R/library/dygraphs/R/dygraphs
/usr/lib64/R/library/dygraphs/R/dygraphs.rdb
/usr/lib64/R/library/dygraphs/R/dygraphs.rdx
/usr/lib64/R/library/dygraphs/examples/examples.R
/usr/lib64/R/library/dygraphs/examples/examples.Rmd
/usr/lib64/R/library/dygraphs/examples/shiny/DESCRIPTION
/usr/lib64/R/library/dygraphs/examples/shiny/server.R
/usr/lib64/R/library/dygraphs/examples/shiny/ui.R
/usr/lib64/R/library/dygraphs/help/AnIndex
/usr/lib64/R/library/dygraphs/help/aliases.rds
/usr/lib64/R/library/dygraphs/help/dygraphs.rdb
/usr/lib64/R/library/dygraphs/help/dygraphs.rdx
/usr/lib64/R/library/dygraphs/help/paths.rds
/usr/lib64/R/library/dygraphs/html/00Index.html
/usr/lib64/R/library/dygraphs/html/R.css
/usr/lib64/R/library/dygraphs/htmlwidgets/dygraphs.js
/usr/lib64/R/library/dygraphs/htmlwidgets/dygraphs.yaml
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/dygraphs/dygraph-combined-dev.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/dygraphs/dygraph-combined.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/dygraphs/dygraph.css
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/dygraphs/shapes.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/fquarter/moment-fquarter.min.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/jquery/AUTHORS.txt
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/timezone/moment-timezone-with-data.js
/usr/lib64/R/library/dygraphs/htmlwidgets/lib/timezone/moment.js
/usr/lib64/R/library/dygraphs/plotters/barchart.js
/usr/lib64/R/library/dygraphs/plotters/barseries.js
/usr/lib64/R/library/dygraphs/plotters/candlestick.js
/usr/lib64/R/library/dygraphs/plotters/candlestickgroup.js
/usr/lib64/R/library/dygraphs/plotters/errorline.js
/usr/lib64/R/library/dygraphs/plotters/errorplotter.js
/usr/lib64/R/library/dygraphs/plotters/filledline.js
/usr/lib64/R/library/dygraphs/plotters/fillplotter.js
/usr/lib64/R/library/dygraphs/plotters/lineplotter.js
/usr/lib64/R/library/dygraphs/plotters/multicolumn.js
/usr/lib64/R/library/dygraphs/plotters/multicolumngroup.js
/usr/lib64/R/library/dygraphs/plotters/stackedbarchart.js
/usr/lib64/R/library/dygraphs/plotters/stackedbargroup.js
/usr/lib64/R/library/dygraphs/plotters/stackedlinegroup.js
/usr/lib64/R/library/dygraphs/plotters/stackedribbongroup.js
/usr/lib64/R/library/dygraphs/plotters/stemplot.js
/usr/lib64/R/library/dygraphs/plugins/compress.js
/usr/lib64/R/library/dygraphs/plugins/crosshair.js
/usr/lib64/R/library/dygraphs/plugins/rebase.js
/usr/lib64/R/library/dygraphs/plugins/ribbon.js
/usr/lib64/R/library/dygraphs/plugins/unzoom.js

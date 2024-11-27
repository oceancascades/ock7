# Download and extract

wget https://zlib.net/current/zlib.tar.gz
tar -xvzf zlib.tar.gz
rm zlib.tar.gz
wget https://github.com/HDFGroup/hdf5/archive/refs/tags/hdf5_1.14.4.2.tar.gz
tar -xvzf hdf5_1.14.4.2.tar.gz
rm hdf5_1.14.4.2.tar.gz
mv hdf5-hdf5_1.14.4.2/ hdf5_1.14.4.2
wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.2.tar.gz
tar -xvzf v4.9.2.tar.gz
rm v4.9.2.tar.gz

# Install zlib

cd zlib-1.3.1/
ZDIR=/usr/local/
./configure --prefix=${ZDIR}
make check
sudo make install

# Install hdf5

cd ../hdf5_1.14.4.2/
H5DIR=/usr/local
./configure --with-zlib=${ZDIR} --prefix=${H5DIR} --enable-hl
make check
sudo make install

# Install netcdf

cd ../netcdf-c-4.9.2/
NCDIR=/usr/local
sudo apt install m4
sudo apt-get install libxml2-dev libxml2-doc
sudo apt-get install libxml2
CPPFLAGS='-I${H5DIR}/include -I${ZDIR}/include' LDFLAGS='-L${H5DIR}/lib -L${ZDIR}/lib' ./configure --prefix=${NCDIR}
make check
sudo make install

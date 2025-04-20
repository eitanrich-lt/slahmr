#!/usr/bin/env bash
set -e

export CONDA_ENV_NAME=slahmr

# Create and activate the conda environment
conda create -n $CONDA_ENV_NAME python=3.10 -y
conda activate $CONDA_ENV_NAME

# Install PyTorch 2.4.0 with CUDA 12.4 support
pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu124

# Set environment variables for CUDA
export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

pip install torch-scatter -f https://data.pyg.org/whl/torch-2.4.0+cu124.html


# install PHALP
pip install phalp[all]@git+https://github.com/brjathu/PHALP.git

# install remaining requirements
pip install -r requirements.txt

# install source
pip install -e .

# install ViTPose
pip install -v -e third-party/ViTPose

# install DROID-SLAM
cd third-party/DROID-SLAM
export TORCH_CUDA_ARCH_LIST="9.0"
python setup.py install
cd ../..

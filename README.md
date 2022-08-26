# Install RAPIDS, TensorFlow, and PyTorch side-by-side

This installation was tested on a T4 and an A10 running Ubuntu 2020.04 LTS. We used Mamba for the install as it's significantly faster than Conda. We only installed the RAPIDS components we needed, in this case `cuDF`, `cuML`, and `cuGraph`. The RAPIDS install also installed `TensorFlow`. Then `PyTorch` was installed into the RAPIDS environment. Expect the entire install process to take under 30 minutes.

## Install

1. [Install CUDA toolkit 11.7](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local)

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda-repo-ubuntu2004-11-7-local_11.7.1-515.65.01-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-7-local_11.7.1-515.65.01-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2004-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

2. [Install Conda](https://docs.conda.io/en/latest/miniconda.html#linux-installers)

```
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
chmod 755 Miniconda3-py39_4.12.0-Linux-x86_64.sh
bash Miniconda3-py39_4.12.0-Linux-x86_64.sh
```

3. [Install Mamba](https://mamba.readthedocs.io/en/latest/installation.html)

```
conda install mamba -n base -c conda-forge
```

4. [Install RAPIDS](https://rapids.ai/start.html#get-rapids)

```
mamba create -n rapids-22.08 -c rapidsai -c nvidia -c conda-forge cudf=22.08 cuml=22.08 cugraph=22.08 python=3.9 cudatoolkit=11.2 tensorflow
conda activate rapids-22.08
```

5. [Install PyTorch](https://pytorch.org/get-started/locally/)

```
mamba install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
```

## Test

Run the following test scripts to validate the install is running as expected.

* [cuML](scripts/hello-cuml.py)
* [cuGraph](scripts/hello-cugraph.py)
* [TensorFlow](scripts/hello-tensorflow.py)
* [PyTorch](scripts/hello-pytorch.py)

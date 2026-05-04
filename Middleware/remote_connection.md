# Remote connection to lab machines

The Computer Architecture lab has two separate clusters that are accessible
through two different front-end nodes available at any time for remote access.
One node is aolin-login.uab.cat and the other one is aoclspv.uab.cat; both
clusters have a SLURM queue system that allows job execution in several
computing nodes.

First, you will need to be logged remotely into head node aoclspv.uab.cat with
your lab account, using the username (for instance, mhedas-x) and password
that was provided to you by your instructor. Remote connection requires the use
of ssh (secure shell), with a non-default port number (443, in this case). You have
to open a terminal window and type this command:

ssh -p 443 mhedas-x@aoclspv.uab.cat

```
Access to the node aolin-login.uab.cat is done in
the same way but using a different port value: 54022.
```
ssh -p 54022 mhedas-x@aolin-login.uab.cat

Regard that in the previous command you have to replace “mhedas-x” with the
specific name of your account (mhedas-1, mhedas-2, ppm-1, ppm-2, biom-1,
biom-2,....). (Note: don’t cut & paste commands from the pdf file; type them
manually).

The first time you log into your account, you may get this dialog:

The authenticity of host '[aoclspv.uab.cat]:443 ([158.109.174.199]:443)' can't be established.
ECDSA key fingerprint is SHA256:29XgrvpJnHUNxAba86SQ/2bsh/dJWUKp9bG6iJBsWwE.
Are you sure you want to continue connecting (yes/no)?

Answer yes. Then the system will ask for your user password:

Warning: Permanently added '[aoclspv.uab.cat]:443,[158.109.174.199]:443' (ECDSA) to the list
of known hosts.
mhedas-1@clus-login.uab.cat's password:

Type your password and, if successfully, you will be logged into the cluster. A
credential dialog may be started before you get the system prompt; just hit
<Enter> key at each question until you get the system prompt.

[mhedas-1@clus-login ~]$

Now you can type any Linux command and it will be executed at the remote
machine. Your interface to the remote machine is limited to the use of the terminal
console (no X-Windows available). File edition can be done using two editors: a
character editor (nano) or a line editor (vim). By typing nano or vim, the
corresponding editor is started and you can write and modify your text files.


NOTE: this section is purely informative, but it may be useful if you have to
connect to remote machines from a Windows machine.

For Windows users, we recommend the use of a third-party tool that provides a
user-friendly interface: MobaXterm (https://mobaxterm.mobatek.net/).

MobaXterm provides both a terminal window and some built-in buttons to transfer
files from/to your local machine and your remote account at aoclspv. Users can
stablish also several ssh connections that are handled in independent tab
screens and there are also many configuration options that simplify connections
to remote hosts.

A basic connection to a remote server is carried out by going to session->SSH.
The following window will open


Fill in this dialog box with the following information:

- Remote host: aoclspv.uab.cat
- Specify username : mhedas-x (check the corresponding box)
- Port : 443

Click OK and the connection will be stablished and a similar dialog to the one
described above will be started (provide you password when requested).

File transfers should use secure copy commands (scp). For instance, to copy a
file from your local machine to the remote machine, type at your local terminal:

scp -P443 your-local-file mhedas-x@aoclspv.uab.cat:.

This command will copy file your-local-file from your current working directory at
your local machine to the home directory of your remote account at aoclspv. To
copy into a remote folder (folder_1) the command would be:

scp -P443 your-local-file mhedas-x@aoclspv.uab.cat:folder_1/.

To copy a file from the remote machine to your local machine, type at your local
terminal:

scp -P443 mhedas-x@aoclspv.uab.cat:your-remote-file.
or
scp -P443 mhedas-x@aoclspv.uab.cat:folder_1/your-remote-file.

First command will copy file your-remote-file from your home directory of your
remote account to the current working directory at your local machine. The
second command will copy the file located at folder_1. Files can be specified with


their complete name but wildchars (such as “*”) can be used to transfer multiple
files at once.

On MobaXterm, clicking the "Scp" tab or “ Sftp” tab (located on the left-hand side
of the MobaXTerm window) opens up a graphical user interface that can be used
for basic file operations. You can drag and drop files in the file explorer or use the
up and down arrows on the toolbar to upload and download files.



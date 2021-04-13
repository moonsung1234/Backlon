
#include "pch.h"
#include "main.h"
#include <iostream>

using namespace std;

int changeBackgroundImage(char* path) {
	cout << "path : " << path << endl;
	
	char full_path[100];
	GetFullPathName(path, 100, full_path, NULL);

	cout << "result : " << full_path << endl;

	return SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, full_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE);
}
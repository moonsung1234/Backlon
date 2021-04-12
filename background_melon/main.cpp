
#include "pch.h"
#include "main.h"
#include <iostream>

using namespace std;

int changeBackgroundImage(char* path) {
	cout << "path : " << path << endl;
	
	return SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE);
}

#pragma once

#ifdef EX
#define EI __declspec(dllexport)
#else
#define EI __declspec(dllimport)
#endif

extern "C" {
	EI int changeBackgroundImage(char* path);
}
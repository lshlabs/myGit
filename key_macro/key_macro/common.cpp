#include "stdafx.h"
#include <Imm.h>
#include "common.h"


#pragma comment (lib, "Version.lib")

void ScreenDependentMousePos (int &mx, int &my)
{
	mx = (int)(mx*GetSystemMetrics(SM_CXSCREEN)/65536.);
	my = (int)(my*GetSystemMetrics(SM_CYSCREEN)/65536.);
}

void ScreenIndependentMousePos (int &mx, int &my)
{
	mx = (mx > 0) ? 
		(int)((mx+0.5)*65536./GetSystemMetrics(SM_CXSCREEN)) : 
		(int)((mx-0.5)*65536./GetSystemMetrics(SM_CXSCREEN)) ;
	my = (my > 0) ? 
		(int)((my+0.5)*65536./GetSystemMetrics(SM_CYSCREEN)) : 
		(int)((my-0.5)*65536./GetSystemMetrics(SM_CYSCREEN)) ;
}

BYTE MouseButton2VkCode (long flags, bool &vk_pressed)
{
	BYTE vk_code = 0;
	vk_pressed = false;

	if      (flags & MOUSEEVENTF_LEFTDOWN)  { vk_code = VK_LBUTTON;  vk_pressed = true;  }
	else if (flags & MOUSEEVENTF_LEFTUP)    { vk_code = VK_LBUTTON;  vk_pressed = false; }
	else if (flags & MOUSEEVENTF_RIGHTDOWN) { vk_code = VK_RBUTTON;  vk_pressed = true;  }
	else if (flags & MOUSEEVENTF_RIGHTUP)   { vk_code = VK_RBUTTON;  vk_pressed = false; }
	else if (flags & MOUSEEVENTF_MIDDLEDOWN){ vk_code = VK_MBUTTON;  vk_pressed = true;  }
	else if (flags & MOUSEEVENTF_MIDDLEUP)  { vk_code = VK_MBUTTON;  vk_pressed = false; }
	else if (flags & MOUSEEVENTF_WHEEL)     { vk_code = ((short)HIWORD(flags) > 0) ? 0x0A : 0x0B; vk_pressed = true; }
	else if (flags & MOUSEEVENTF_XDOWN) {
		if (HIWORD(flags) & XBUTTON1)		{ vk_code = VK_XBUTTON1; vk_pressed = true;  }
		if (HIWORD(flags) & XBUTTON2)		{ vk_code = VK_XBUTTON2; vk_pressed = true;  }
	}
	else if (flags & MOUSEEVENTF_XUP) {
		if (HIWORD(flags) & XBUTTON1)		{ vk_code = VK_XBUTTON1; vk_pressed = false; }
		if (HIWORD(flags) & XBUTTON2)		{ vk_code = VK_XBUTTON2; vk_pressed = false; }
	}
	return vk_code;
}

bool IsImeHangul()
{
	// ���� IME ���°� �ѱ����� �������� üũ�Ѵ�.

	HWND hWnd = ::GetForegroundWindow();
	if (hWnd) {
		HWND hWndIme = ImmGetDefaultIMEWnd(hWnd);
		if (hWndIme) {
			int ret = ::SendMessage(hWndIme, WM_IME_CONTROL, 0x5, 0);
			return ret ? true : false;
		}
	}
	return false;
}

void SetImeHangul (bool hangul)
{
	// IME�� �ѱ��̳� �������� ��ȯ�Ѵ�.
	// �� ���� �ȹٲ�� ��찡 �����Ƿ�, �ȹٲ�°�� 10�� �õ��Ѵ�.

	for (int i=0; i<10; i++) {
		if (IsImeHangul() != hangul) {
			keybd_event (VK_HANGUL, MapVirtualKey (VK_HANGUL, MAPVK_VK_TO_VSC), KEYEVENTF_EXTENDEDKEY, EX_KEY_MACRO_ITSELF);
			Sleep (33);
			keybd_event (VK_HANGUL, MapVirtualKey (VK_HANGUL, MAPVK_VK_TO_VSC), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, EX_KEY_MACRO_ITSELF);
			Sleep (33);
		}
	}
}

void ReleaseAllKeys (bool vk_pressed[256])
{
	// vk_pressed �迭���� true �� ���, Key up �̺�Ʈ�� ������.
	for (int vk_index=0; vk_index<256; vk_index++) {
		if (vk_pressed[vk_index]) {
			switch (vk_index) {
			case VK_LBUTTON:  mouse_event (MOUSEEVENTF_LEFTUP,   0, 0, 0,        EX_KEY_MACRO_ITSELF);	break;
			case VK_RBUTTON:  mouse_event (MOUSEEVENTF_RIGHTUP,  0, 0, 0,        EX_KEY_MACRO_ITSELF);	break;
			case VK_MBUTTON:  mouse_event (MOUSEEVENTF_MIDDLEUP, 0, 0, 0,        EX_KEY_MACRO_ITSELF);	break;
			case VK_XBUTTON1: mouse_event (MOUSEEVENTF_XUP,		 0, 0, XBUTTON1, EX_KEY_MACRO_ITSELF);	break;
			case VK_XBUTTON2: mouse_event (MOUSEEVENTF_XUP,		 0, 0, XBUTTON2, EX_KEY_MACRO_ITSELF);	break;
			default:          keybd_event (vk_index, MapVirtualKey (vk_index, MAPVK_VK_TO_VSC), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, EX_KEY_MACRO_ITSELF); break;
			}
		}
	}
	memset (vk_pressed, 0, sizeof(bool)*256);
}

void ReleaseAllKeys ()
{
	// ��� ���� Ű�� ���� �Ѵ�.
	GetKeyState(0); // Windows - Dev Center ���򸻿� ���ϸ�... 
	// GetKeyboardState()�� �����ϱ� ���� GetKeyState() �� ȣ���ؾ� ���� �����Ѵٰ� ��.

	BYTE keyState[256];
	GetKeyboardState((LPBYTE)&keyState);

	for (int vk_index=0; vk_index<256; vk_index++) {
		if (keyState[vk_index] & 0x80) {	// ���� �����̸�
			keybd_event (vk_index, MapVirtualKey (vk_index, MAPVK_VK_TO_VSC), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, EX_KEY_MACRO_ITSELF);
		}
	}
}

bool ApplicationAlreadyExist (char *WindowClass, char *Title)
{
	// ���� ���α׷��� ���� ���� ������ üũ�Ѵ�.

	HANDLE hMutex = CreateMutex(NULL, TRUE, Title);   // Create mutex
	switch(GetLastError()) {
	case ERROR_SUCCESS:			break;
	case ERROR_ALREADY_EXISTS:	return true;
	default:					return false;
	}
	return false;
}

CString GetVersionInfo(CString csEntry)
{
	// ���ҽ����� ���� ������ �����´�.
	CString csRet = "";

	HRSRC hResInfo = FindResource (NULL, MAKEINTRESOURCE(VS_VERSION_INFO), RT_VERSION);
	
	if (hResInfo) {
		HGLOBAL hResData = LoadResource (NULL, hResInfo);
		DWORD dwSize = SizeofResource (NULL, hResInfo);

		if (hResData) {
			LPVOID pRes = LockResource (hResData);

			if (pRes) {
				// ���ҽ��� ���� ������ �� �� ����. �޸𸮸� ������ �´�.
				LPVOID pResCopy = LocalAlloc(LMEM_FIXED, dwSize+1000);	// dwSize���� �� ũ��... VerQueryValue() �Լ��� pResCopy �޸𸮿� ������ ���µ�
				CopyMemory (pResCopy, pRes, dwSize);
				UnlockResource (hResData);
				FreeResource (hResData);

				UINT vLen;
				LPVOID retbuf = NULL;
				char query[256];

				BOOL retVal = VerQueryValue (pResCopy, "\\VarFileInfo\\Translation", &retbuf, &vLen);
				if (retVal && vLen==4) {
					DWORD langD = *(DWORD *)retbuf;
	
					sprintf(query, "\\StringFileInfo\\%02X%02X%02X%02X\\%s",
						(langD>> 8)&0xFF, (langD>> 0)&0xFF, (langD>>24)&0xFF, (langD>>16)&0xFF, (LPCTSTR)csEntry);
				}
				else {
					sprintf(query, "\\StringFileInfo\\%04X04B0\\%s", GetUserDefaultLangID(), (LPCTSTR)csEntry);
				}

				retVal = VerQueryValue (pResCopy, query, &retbuf, &vLen);
				if (retVal) {
					csRet = (char*)retbuf;
				}

				LocalFree(pResCopy);
			}
		}
	}

	return csRet;
}
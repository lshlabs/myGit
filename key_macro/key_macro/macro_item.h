#pragma once

enum eMacroType { MI_NONE = 0, MI_KEY, MI_MOUSE, MI_DELAY };


struct sKeybd {
	// High BYTE - Scan code
	// Low BYTE - Virtual key code
	long scan_vk_code;
	// 0x01 - ������
	// 0x02 - ����
	// 0x03 - ������ ����
	// 0x10 - �ѱ� �Է� ����, �� ��Ʈ�� 0�� ��� ���� �Է� ����
	// 0x20 - Extended key�� ����, �� ��Ʈ�� 0�� ��� �Ϲ� Ű
	unsigned long flags;

	void Step (bool vk_pressed[256]);
};

struct sMouse {
	long x, y;	// ���콺 Ŀ���� ��ġ
	// Low WORD:
	//	 MOUSEEVENTF_MOVE        0x0001 // mouse move 
	//	 MOUSEEVENTF_LEFTDOWN    0x0002 // left button down 
	//	 MOUSEEVENTF_LEFTUP      0x0004 // left button up 
	//	 MOUSEEVENTF_RIGHTDOWN   0x0008 // right button down 
	//	 MOUSEEVENTF_RIGHTUP     0x0010 // right button up 
	//	 MOUSEEVENTF_MIDDLEDOWN  0x0020 // middle button down 
	//	 MOUSEEVENTF_MIDDLEUP    0x0040 // middle button up 
	//	 MOUSEEVENTF_XDOWN       0x0080 // x button down (XBUTTON 1,2�� High byte���� ����)
	//	 MOUSEEVENTF_XUP         0x0100 // x button down 
	//	 MOUSEEVENTF_WHEEL       0x0800 // wheel button rolled 
	// High WORD:
	//	 XBUTTON1, XBUTTON2, ���� ���� ��
	unsigned long flags;

	void Step (bool vk_pressed[256]);
};

struct sDelay {
	long delay; // ���� �ð� ���, ����: msec

	bool Step (long &delay_count, long dt);
};

struct sMacroItem {
	eMacroType type;

	union {
		sKeybd keybd;
		sMouse mouse;
		sDelay delay;
		long   data[3];
	};

	sMacroItem () : type(MI_NONE) 
	{ 
		data[0] = data[1] = data[2] = 0;
	}
	
	sMacroItem (const sMacroItem &mi) {
		type = mi.type;
		data[0] = mi.data[0];
		data[1] = mi.data[1];
		data[2] = mi.data[2];
	}
	
	sMacroItem &operator = (const sMacroItem &mi) {
		if (this != &mi) {
			type = mi.type;
			data[0] = mi.data[0];
			data[1] = mi.data[1];
			data[2] = mi.data[2];
		}
		return *this;
	}
};

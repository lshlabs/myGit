#pragma once
#include "common.h"
#include "macro_item.h"
#include <vector>

using namespace std;

#define VK_KEY_UP			0x00010000
#define VK_KEY_MASK			0x000000FF

struct sMacro {
	char name[256];			// ��ũ�� �̸�
	long start_key;			// ��ũ�� ���� Ű, 0x10000 - Ű �� ��
	long stop_key;			// ��ũ�� ���� Ű, 0x10000 - Ű �� ��
	long repeat_cnt;		// ��ũ�� �ݺ����� Ƚ��(0�̸� ���ѹݺ�)

	vector<sMacroItem> _item;

	// ��ũ�� ����� �ʿ��� ������
	long index;				// Ű����/���콺 �̺�Ʈ�� ���� ����
	long delay;				// �����ð� ī��Ʈ�� ���
	long run_count;			// ��ũ�� ���� Ƚ�� ī��Ʈ
	bool vk_pressed[256];	// Virtual key code�� ������ �� true

	void init ();
	void start (int index_ = 1);
	void stop ();

	bool is_running()
	{
		return 0 <= index && index < (int)_item.size();
	}

	sMacro () : 
		start_key(0), 
		stop_key(0), 
		repeat_cnt(1) 
	{
		init();
		name[0] = '\0';
	}
	
	sMacro (const sMacro &macro) 
	{
		strncpy (name, macro.name, 256);
		name[256-1] = '\0';
		start_key	= macro.start_key;
		stop_key	= macro.stop_key;
		repeat_cnt	= macro.repeat_cnt;
		_item = macro._item;

		init ();
	}

	sMacro &operator = (const sMacro &macro) 
	{
		if (this != &macro) {
			strncpy (name, macro.name, 256);
			name[256-1] = '\0';
			start_key	= macro.start_key;
			stop_key	= macro.stop_key;
			repeat_cnt	= macro.repeat_cnt;
			_item = macro._item;

			init ();
		}
		return *this;
	}
};

extern vector<sMacro> g_macros;

extern void MacroInit ();
extern void MacroTerm ();

extern void AllMacroStep (int dt);
extern void MacroStep (sMacro &m, int dt);

extern void MacroStartStopShortkey (BYTE vk_code, bool vk_pressed);


#include "StdAfx.h"
#include "macro_def.h"
#include "virtual_key.h"
#include "AppIni.h"


const char *strKeyboardOption (int flags)
{
	switch (flags) {
	case 0x00: return "";
	case 0x01: return "������";
	case 0x02: return "����";
	case 0x03: return "";
	default:   return "(����)";
	}
}

const char *strMouseOption (int flags)
{
	switch (flags) {
	case 0x00: return "";
	case 0x01: return "������";
	case 0x02: return "����";
	case 0x03: return "Ŭ��";
	default:   return "(����)";
	}
}

const char *GetItemDescription (const sMacroItem &item)
{
	int n = 0;
	static char desc[256];	// ���ڿ��� �����ؾ� �ϱ⶧���� static���� �����Ѵ�.
	desc[0] = '\0';

	switch (item.type) {
	case MI_NONE: 
		n = sprintf (desc, "(����)");
		break;

	case MI_KEY: {
		int index = GetVkIndex(LOBYTE(item.keybd.scan_vk_code));
		n = sprintf (desc, "Ű���� %s ", GetVkDesc(index));
		if (item.keybd.flags) { 
			n += sprintf (desc + n, "%s ", strKeyboardOption(item.keybd.flags&0x03));
			if (g_ini.macroOptions.CHECK_IME_HAN_ENG) {
				n += sprintf (desc + n, "[%s] ", (item.keybd.flags&0x10) ? "�ѱ�" : "����");
			}
		}
		break; }

	case MI_MOUSE: {
		n = sprintf (desc, "���콺 ");
		if (item.mouse.flags & MOUSEEVENTF_MOVE) {
			n += sprintf (desc + n, "��ġ(%d, %d) ", item.mouse.x, item.mouse.y);
		}

		if (item.mouse.flags & MOUSEEVENTF_WHEEL) {
			n += sprintf (desc + n, "��(%d) ", (int)(short)HIWORD(item.mouse.flags));
		}

		int flags = (item.mouse.flags>>1) & 0x03;
		if (flags) n += sprintf (desc + n, "�޹�ư_%s ", strMouseOption(flags));

		flags = (item.mouse.flags>>3) & 0x03;
		if (flags) n += sprintf (desc + n, "������ư_%s ", strMouseOption(flags));

		flags = (item.mouse.flags>>5) & 0x03;
		if (flags) n += sprintf (desc + n, "�߾ӹ�ư_%s ", strMouseOption(flags));

		flags = (item.mouse.flags>>7) & 0x03;
		if (flags) {
			if (HIWORD(item.mouse.flags) == XBUTTON1) {
				n += sprintf (desc + n, "X1��ư_%s ", strMouseOption(flags));
			}
			if (HIWORD(item.mouse.flags) == XBUTTON2) {
				n += sprintf (desc + n, "X2��ư_%s ", strMouseOption(flags));
			}
		}
		break; }

	case MI_DELAY:
		n = sprintf (desc, "�ð����� %0.3f ��", (double)item.delay.delay/1000.);
		break;
	}

	return desc;
}


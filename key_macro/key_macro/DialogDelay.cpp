#include "stdafx.h"
#include "key_macro.h"
#include "DialogDelay.h"
#include "Common.h"

// ���α׷��� ����Ǵ� ���� ��ȭ���� �����ۿ� 
// ������ ���� �����ϰ� �ִ� �������� static���� ����
static long _delay = 1000;

IMPLEMENT_DYNAMIC(CDialogDelay, CDialog)

CDialogDelay::CDialogDelay(CWnd* pParent /*=NULL*/)
	: CDialogCommon (CDialogDelay::IDD, pParent)
{
}

CDialogDelay::~CDialogDelay()
{
}

void CDialogDelay::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}


BEGIN_MESSAGE_MAP(CDialogDelay, CDialog)
	ON_BN_CLICKED(IDOK, &CDialogDelay::OnBnClickedOk)
END_MESSAGE_MAP()


BOOL CDialogDelay::OnInitDialog()
{
	CDialog::OnInitDialog();

	if (_item.type == MI_NONE) {
		SetWindowText ("�ð� ���� �߰�");
		// �⺻�� ����
		_item.type = MI_DELAY;
		_item.delay.delay = _delay;
	}
	else {
		SetWindowText ("�ð� ���� ����");
	}

	SetDlgItemDouble (IDC_EDIT_DELAY, (double)_item.delay.delay/1000.);

	return TRUE;  // return TRUE unless you set the focus to a control
	// EXCEPTION: OCX Property Pages should return FALSE
}

void CDialogDelay::OnBnClickedOk()
{
	_delay = (int)(1000*GetDlgItemDouble (IDC_EDIT_DELAY));
	_delay = BOUND(_delay, 1L, 86400000L);

	_item.delay.delay = _delay;

	OnOK();
}

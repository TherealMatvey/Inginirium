#include <iostream>
#include <random>
using namespace std;


class Enemy
{
	protected:
		int attackpower;
	public:
		void setAttackPower(int a)
		{
			attackpower = a;
		}
};

class Ninja: public Enemy
{
	public:
		void attack()
		{
			cout << "Ninja! " << attackpower << "hp" << endl;
		}

};

class Monster : public Enemy
{
	public:
		void attack()
		{
			cout << "Monster " << attackpower << "hp" << endl;
		}
};


class Defender
{
protected:
	int attackpowhero;
public:
	void setAttackPowHero(int b)
	{
		attackpowhero = b;
	}
};

class Sniper: public Defender
{
public:
	void shield()
	{
		cout << "Sniper -> Ninja -" << attackpowhero << endl;
	}

};

class Superman : public Defender
{
public:
	void shield()
	{
		cout << "Superman -> Monster -" << attackpowhero << endl;
	}
};

int main()
{
	srand(time (NULL));
	Ninja n;
	Monster m;
	Sniper i;
	Superman j;

	int q = 20;
	int w = 80;

	int e = rand() % 21;
	int r = rand() % 81;

	n.setAttackPower(q);
	m.setAttackPower(w);

	i.setAttackPowHero(e);
	j.setAttackPowHero(r);

	n.attack();
	m.attack();
	cout << endl;
	i.shield();
	j.shield();
	cout << endl;
	n.setAttackPower(q - e);
	m.setAttackPower(w - r);
	n.attack();
	m.attack();


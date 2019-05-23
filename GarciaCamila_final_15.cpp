#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#define PI 3.14159
using namespace std;

#define TAB "\t"

const double m = 7294.29;
const double q = 2.0;
double dt = 0.001;

double rad(double teta){
	return PI*teta/180.0;
}

double velx(double t,double x, double y, double vx, double vy){
	return vx;
}

double vely(double t,double x, double y, double vx, double vy){
	return vy;
}


double acx( double t,double x, double y, double vx, double vy){
	return m*vx ;
}

double acy(double t,double x, double y, double vx, double vy){
	return m*vy ;
}


void RungeKutta(double &t, double &x, double &y, double &vx, double &vy, double &m, double &q){
	double primerpaso1,primerpaso2,primerpaso3, primerpaso4;
	primerpaso1=dt*velx(t,x,y,vx,vy);
	primerpaso2=dt*vely(t,x,y,vx,vy);
	primerpaso3=dt*acx(t,x,y,vx,vy);
	primerpaso4=dt*acy(t,x,y,vx,vy);
	double segundopaso1,segundopaso2,segundopaso3,segundopaso4;
	segundopaso1=dt*velx(t+(1/2)*dt,x+(1/2)*primerpaso1,y+(1/2)*primerpaso2,vx+(1/2)*primerpaso3,vy+(1/2)*primerpaso4);
	segundopaso2=dt*vely(t+(1/2)*dt,x+(1/2)*primerpaso1,y+(1/2)*primerpaso2,vx+(1/2)*primerpaso3,vy+(1/2)*primerpaso4);
	segundopaso3=dt*acx(t+(1/2)*dt,x+(1/2)*primerpaso1,y+(1/2)*primerpaso2,vx+(1/2)*primerpaso3,vy+(1/2)*primerpaso4);
	segundopaso4=dt*acy(t+(1/2)*dt,x+(1/2)*primerpaso1,y+(1/2)*primerpaso2,vx+(1/2)*primerpaso3,vy+(1/2)*primerpaso4);
	double tercerpaso1,tercerpaso2,tercerpaso3,tercerpaso4;
	tercerpaso1=dt*velx(t+(1/2)*dt,x+(1/2)*segundopaso1,y+(1/2)*segundopaso2,vx+(1/2)*segundopaso3,vy+(1/2)*segundopaso4);
	tercerpaso2=dt*vely(t+(1/2)*dt,x+(1/2)*segundopaso1,y+(1/2)*segundopaso2,vx+(1/2)*segundopaso3,vy+(1/2)*segundopaso4);
	tercerpaso3=dt*acx(t+(1/2)*dt,x+(1/2)*segundopaso1,y+(1/2)*segundopaso2,vx+(1/2)*segundopaso3,vy+(1/2)*segundopaso4);
	tercerpaso4=dt*acy(t+(1/2)*dt,x+(1/2)*segundopaso1,y+(1/2)*segundopaso2,vx+(1/2)*segundopaso3,vy+(1/2)*segundopaso4);
	double cuartopaso1,cuartopaso2,cuartopaso3,cuartopaso4;
	cuartopaso1=dt*velx(t+dt,x+tercerpaso1,y+tercerpaso2,vx+tercerpaso3,vy+tercerpaso4);
	cuartopaso2=dt*vely(t+dt,x+tercerpaso1,y+tercerpaso2,vx+tercerpaso3,vy+tercerpaso4);
	cuartopaso3=dt*acx(t+dt,x+tercerpaso1,y+tercerpaso2,vx+tercerpaso3,vy+tercerpaso4);
	cuartopaso4=dt*acy(t+dt,x+tercerpaso1,y+tercerpaso2,vx+tercerpaso3,vy+tercerpaso4);
	t+=dt;
	x+=(primerpaso1+2*(segundopaso1+tercerpaso1)+cuartopaso1)*(1/6.0);
	y+=(primerpaso2+2*(segundopaso2+tercerpaso2)+cuartopaso2)*(1/6.0);
	vx+=(primerpaso3+2*(segundopaso3+tercerpaso3)+cuartopaso3)*(1/6.0);
	vy+=(primerpaso4+2*(segundopaso4+tercerpaso4)+cuartopaso4)*(1/6.0);
}



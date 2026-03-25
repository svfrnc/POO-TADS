package Aula 04;

class circulo:
    private double raio = 0
    public void setRaio(double v) {
        if (v >= 0) this.raio = v;
        else throw new IlllegalArgumentException ("Valor inválido");
    } 


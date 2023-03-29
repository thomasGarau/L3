package exo3;

public class PreLoad extends Event {

	public PreLoad() {
		super("preLoad");
	}

	public void traiter(EventInterceptor ei, Object entity){
		ei.preLoad(entity);
	}

}
